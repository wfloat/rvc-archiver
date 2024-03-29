# Seed the database with new data from https://docs.google.com/spreadsheets/d/1leF7_c2Qf5iQRVkmOF51ZSynOvEjz8fHqwriX1wUMPw/edit#gid=537336172
import os
import json
from tqdm import tqdm
from dotenv import load_dotenv
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from graphql.generated.schema import CreateAIHubVoiceModelInput
from graphql.generated.operations import Operations
from util.google_sheet import get_sheet_rows, AIHubSheetRow
from urllib.parse import urlparse, urlunparse
from openai import OpenAI
import json
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
import zipfile
import requests
import shutil
import hashlib
import optuna
from util.optimize_params import (
    objective,
    TRANSPOSE_PITCH,
    F0_CURVE,
    AUDIO_RESAMPLING,
    PITCH_EXTRACTION_METHOD,
)
from concurrent.futures import ThreadPoolExecutor
from functools import partial

load_dotenv()


# Load model metadata from spreadsheet
GOOGLE_DOC_ID = os.environ.get("DOC_ID")
GOOGLE_SHEET_ID = os.environ.get("SHEET_ID")

WFLOAT_API_URL = os.getenv("WFLOAT_API_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

VOICE_MODEL_PROFILES_OUTPUT_DIR = "profiles"
VOICE_MODEL_WEIGHTS_OUTPUT_DIR = "model-zips"
VOICE_MODEL_SHARED_DIR = "shared"

OPTUNA_SHOW_PROGRESS_BAR = False
OPTIMIZATION_TRIAL_COUNT = 100
# GRADIO_SERVER_URL = "http://localhost:7865/"
MAX_WORKER_THREADS = 3
# TODO: Figure out why 3 threads is the sweet spot for optimizing the models in parallel and not more
GRADIO_SERVER_PORTS = [
    "7865",
    "7866",
    "7867",
    # "7868",
    # "7869",
    # "7870",
    # "7871",
    # "7872",
]

assert MAX_WORKER_THREADS == len(GRADIO_SERVER_PORTS)

endpoint = HTTPEndpoint(WFLOAT_API_URL)


@dataclass
class VoiceModelProfile:
    confidence: Optional[float] = None
    fameLevel: Optional[float] = None
    fictional: Optional[bool] = None
    name: Optional[str] = None
    gender: Optional[str] = None
    relevantTags: Optional[List[str]] = None
    accent: Optional[str] = None
    nativeLanguage: Optional[str] = None
    modelTrainedOnEnglishProbability: Optional[float] = None


def remove_carriage_returns(input_str: str) -> str:
    if input_str is None:
        return ""
    return input_str.replace("\r", "")


def standardize_url(url: str) -> str:
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme.lower()
    netloc = parsed_url.netloc.lower()
    if ":" in netloc:
        hostname, port = netloc.split(":")
        if (scheme == "http" and port == "80") or (scheme == "https" and port == "443"):
            netloc = hostname
    path = parsed_url.path
    query = "&".join(sorted(parsed_url.query.split("&")))
    return urlunparse((scheme, netloc, path, "", query, ""))


def safe_unzip(zip_path, extract_to_folder, size_limit):
    total_size = 0
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        for file_info in zip_ref.infolist():
            total_size += file_info.file_size
            if total_size > size_limit:
                raise Exception("Size limit exceeded, aborting unzipping.")
            zip_ref.extract(file_info, extract_to_folder)


def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)


def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


def chunk_it(seq, num):
    """Yield successive n-sized chunks from seq."""
    avg = len(seq) / float(num)
    last = 0.0
    while last < len(seq):
        yield seq[int(last) : int(last + avg)]
        last += avg


def populate_aihub_voice_model_and_voice_model_backup_url_tables(
    sheet_rows: List[AIHubSheetRow],
):
    create_aihub_voice_model = Operations.mutation.create_aihub_voice_model

    create_voice_model_backup_url = Operations.mutation.create_voice_model_backup_url

    for sheet_row in tqdm(sheet_rows):
        if sheet_row.rvc_version != "RVC v2":
            continue
        if sheet_row.md5_hash == None:
            continue

        filename = remove_carriage_returns(sheet_row.filename)
        model_name = remove_carriage_returns(sheet_row.model_name)
        if model_name == "":
            model_name = None
        if filename == "":
            continue

        input_data = {
            "downloadCount": sheet_row.download_counter,
            "filename": filename,
            "name": model_name,
            "version": sheet_row.rvc_version,
            "checksumMD5ForWeights": sheet_row.md5_hash,
            # "creatorText": # TODO: pull in creatorText from the "Oranized Model List w/ Credits" spreadsheet
        }

        res = endpoint(query=create_aihub_voice_model, variables={"input": input_data})

        errors = res.get("errors")
        if errors:
            continue

        aihub_voice_model = res["data"]["createAIHubVoiceModel"]

        # print(data)

        model_id = aihub_voice_model["id"]

        if sheet_row.url:
            url_standardized = standardize_url(sheet_row.url)
            if url_standardized == "":
                url_standardized = None

            input_data = {"url": url_standardized, "voiceModelId": model_id}
            res = endpoint(
                query=create_voice_model_backup_url, variables={"input": input_data}
            )
            errors = res.get("errors")
            # if errors:
            #     print(errors)

        for i in range(1, 20):
            alt_url_field = f"alt_url{i}"
            alt_url_value = getattr(sheet_row, alt_url_field, None)

            if alt_url_value:
                alt_url_standardized = standardize_url(alt_url_value)
                if alt_url_standardized == "":
                    alt_url_standardized = None

                input_data = {
                    "url": alt_url_standardized,
                    "voiceModelId": model_id,
                }
                res = endpoint(
                    query=create_voice_model_backup_url,
                    variables={"input": input_data},
                )
                errors = res.get("errors")
                # if errors:
                #     print(errors)


def generate_voice_model_profiles_with_openai(output_dir: str):
    aihub_voice_models_query = Operations.query.aihub_voice_models
    page_end_cursor = None
    has_next_page = True

    aihub_voice_models = []

    while has_next_page:
        res = endpoint(
            query=aihub_voice_models_query, variables={"after": page_end_cursor}
        )

        errors = res.get("errors")
        if errors:
            continue

        aihub_voice_model_connection = res["data"]["AIHubVoiceModels"]
        page_end_cursor = aihub_voice_model_connection["pageInfo"]["endCursor"]
        has_next_page = aihub_voice_model_connection["pageInfo"]["hasNextPage"]

        for edge in aihub_voice_model_connection["edges"]:
            aihub_voice_models.append(edge["node"])

    client = OpenAI(
        # This is the default and can be omitted
        api_key=OPENAI_API_KEY,
    )

    for aihub_voice_model in tqdm(aihub_voice_models):
        weights_name = f"'{aihub_voice_model['filename']}'"
        model_name = aihub_voice_model["name"]

        if model_name == None:
            model_name = "None"
        else:
            model_name = f"'{model_name}'"

        prompt = f"Given the following data VoiceModelData = {{ model_name: {model_name}, weights_name: {weights_name}, }} I want you to make your best guess at filling in the following JSON of who this voice model represents. Note that the model name and weights name can contain metadata including but not limited to epochs/creation date/author name/dataset source that may or may not be directly useful to identifying who the voice model represents. The voice can be a fictional character or a real person. ProfileOrCharacter = {{ confidence: float # score 0.0 to 1.0 \n fameLevel: float # score 0.0 to 1.0 \n fictional: bool \n name: str \n gender: str # male or female \n relevantTags: str[] # if not None: minimum 5/maximum 10 \n accent: str \n nativeLanguage: str \n modelTrainedOnEnglishProbability: float }} I need you to output only the filled in object. If identity is unknown, set fields to null"

        chat_completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        response = json.loads(chat_completion.choices[0].message.content)

        md5_hash = aihub_voice_model["checksumMD5ForWeights"]
        voice_profile_path = f"{output_dir}/{md5_hash}.json"
        with open(voice_profile_path, "w") as file:
            json.dump(response, file)


def populate_voice_model_profile_table(profiles_dir: str):
    aihub_voice_model_using_checksum_md5_for_weights_query = (
        Operations.query.aihub_voice_model_using_checksum_md5_for_weights
    )

    create_voice_model_profile = Operations.mutation.create_voice_model_profile

    for filename in tqdm(os.listdir(profiles_dir)):
        if filename.endswith(".json"):
            with open(os.path.join(profiles_dir, filename), "r") as file:
                data = json.load(file)
                voice_model_profile = VoiceModelProfile(**data)

                all_fields_set = all(
                    getattr(voice_model_profile, field) is not None
                    for field in voice_model_profile.__dict__
                )
                if all_fields_set:
                    res = endpoint(
                        query=aihub_voice_model_using_checksum_md5_for_weights_query,
                        variables={"checksumMD5ForWeights": filename.rstrip(".json")},
                    )
                    errors = res.get("errors")
                    if errors:
                        print(errors)

                    if not errors:
                        aihub_voice_model = res["data"]["AIHubVoiceModel"]

                        input_data = {
                            "confidence": voice_model_profile.confidence,
                            # "fameLevel": voice_model_profile.fameLevel, # TODO: Consider this to the API
                            "fictional": voice_model_profile.fictional,
                            "name": voice_model_profile.name,
                            "gender": voice_model_profile.gender,
                            "relevantTags": voice_model_profile.relevantTags,
                            "accent": voice_model_profile.accent,
                            "nativeLanguage": voice_model_profile.nativeLanguage,
                            "modelTrainedOnEnglishProbability": voice_model_profile.modelTrainedOnEnglishProbability,
                            "voiceModelId": aihub_voice_model["id"],
                        }
                        res = endpoint(
                            query=create_voice_model_profile,
                            variables={"input": input_data},
                        )
                        errors = res.get("errors")
                        if errors:
                            print(errors)


def download_voice_model_weights(weights_output_dir: str):
    aihub_voice_models_query = Operations.query.aihub_voice_models
    page_end_cursor = None
    has_next_page = True

    aihub_voice_models = []

    while has_next_page:
        res = endpoint(
            query=aihub_voice_models_query, variables={"after": page_end_cursor}
        )

        errors = res.get("errors")
        if errors:
            continue

        aihub_voice_model_connection = res["data"]["AIHubVoiceModels"]
        page_end_cursor = aihub_voice_model_connection["pageInfo"]["endCursor"]
        has_next_page = aihub_voice_model_connection["pageInfo"]["hasNextPage"]

        for edge in aihub_voice_model_connection["edges"]:
            aihub_voice_models.append(edge["node"])

    # random.shuffle(aihub_voice_models)
    for aihub_voice_model in tqdm(aihub_voice_models):
        inferred_profile = aihub_voice_model["inferredProfile"]
        if not inferred_profile:
            continue

        if (
            inferred_profile["nativeLanguage"] != "English"
            or inferred_profile["accent"] != "American"
        ):
            potentially_dubbed = "anime" in [
                element.lower() for element in inferred_profile["relevantTags"]
            ]
            if not potentially_dubbed:
                continue

        backup_urls = []
        for edge in aihub_voice_model["backupUrls"]["edges"]:
            backup_urls.append(edge["node"]["url"])
        if len(backup_urls) == 0:
            continue
        backup_urls = sorted(backup_urls, key=lambda url: "huggingface" not in url)

        contains_huggingface = any("huggingface" in url for url in backup_urls)
        if not contains_huggingface:
            continue
        try:
            download_file(
                backup_urls[0],
                f"{weights_output_dir}/{aihub_voice_model['checksumMD5ForWeights']}.zip",
            )
        except Exception as e:
            print(
                f"Error downloading weights for {inferred_profile['name']} MD5: {aihub_voice_model['checksumMD5ForWeights']}\n{e}"
            )


def populate_voice_model_table_and_build_weights_folder_structure(
    weights_in_dir: str, weights_structured_dir: str
):
    tmp_dir = "./tmp"
    zip_size_limit = 786432000  # in bytes
    aihub_voice_model_using_checksum_md5_for_weights_query = (
        Operations.query.aihub_voice_model_using_checksum_md5_for_weights
    )
    create_voice_model = Operations.mutation.create_voice_model
    update_aihub_voice_model = Operations.mutation.update_aihub_voice_model

    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    weights_dir = os.path.join(weights_structured_dir, "weights")
    logs_dir = os.path.join(weights_structured_dir, "logs")
    if not os.path.exists(weights_dir):
        os.makedirs(weights_dir)
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    for zip_file in tqdm(os.listdir(weights_in_dir)):
        if zip_file.endswith(".zip"):
            zip_path = os.path.join(weights_in_dir, zip_file)
            try:
                safe_unzip(zip_path, tmp_dir, zip_size_limit)
            except Exception as e:
                print(f"Error unzipping {zip_path}\n{e}")
                continue

            # Now check the tmp directory and potentially one folder deep for the required files
            for root, dirs, files in os.walk(tmp_dir):
                md5_weights_file_hash = None
                md5_added_file_hash = None
                sha256_weights_file_hash = None
                sha256_added_file_hash = None
                weights_file_size = None
                added_file_size = None

                for file in files:
                    if file.endswith(".pth"):
                        weights_file_path = os.path.join(root, file)
                        md5_weights_file_hash = get_md5(weights_file_path)
                        sha256_weights_file_hash = get_sha256(weights_file_path)
                        weights_file_size = os.path.getsize(weights_file_path)

                        if md5_weights_file_hash != zip_file.rstrip(".zip"):
                            break

                        shutil.move(
                            weights_file_path,
                            os.path.join(
                                weights_dir, f"{sha256_weights_file_hash}.pth"
                            ),
                        )

                if (
                    sha256_weights_file_hash
                    and md5_weights_file_hash == zip_file.rstrip(".zip")
                ):
                    for file in files:
                        if file.endswith(".index"):
                            added_file_path = os.path.join(root, file)
                            md5_added_file_hash = get_md5(added_file_path)
                            sha256_added_file_hash = get_sha256(added_file_path)
                            added_file_size = os.path.getsize(added_file_path)

                            shutil.move(
                                added_file_path,
                                os.path.join(
                                    logs_dir, f"{sha256_weights_file_hash}.index"
                                ),
                            )

                            res = endpoint(
                                query=aihub_voice_model_using_checksum_md5_for_weights_query,
                                variables={
                                    "checksumMD5ForWeights": md5_weights_file_hash
                                },
                            )
                            errors = res.get("errors")
                            if errors:
                                print()
                            if not errors:
                                aihub_voice_model = res["data"]["AIHubVoiceModel"]
                                voice_model_name = aihub_voice_model["inferredProfile"][
                                    "name"
                                ]

                                input_data = {
                                    "checksumMD5ForAdded": md5_added_file_hash,
                                    "checksumMD5ForWeights": md5_weights_file_hash,
                                    "checksumSHA256ForAdded": sha256_added_file_hash,
                                    "checksumSHA256ForWeights": sha256_weights_file_hash,
                                    "filesizeForWeights": weights_file_size,
                                    "filesizeForAdded": added_file_size,
                                    "hidden": True,
                                    "name": voice_model_name,
                                    "processed": False,
                                }

                                res = endpoint(
                                    query=create_voice_model,
                                    variables={"input": input_data},
                                )

                                errors = res.get("errors")
                                if errors:
                                    print()

                                # Update AIHubVoiceModel record with derivedModelId
                                if not errors:
                                    voice_model = res["data"]["createVoiceModel"]

                                    input_data = {
                                        "id": aihub_voice_model["id"],
                                        "derivedModelId": voice_model["id"],
                                    }
                                    res = endpoint(
                                        query=update_aihub_voice_model,
                                        variables={"input": input_data},
                                    )

                                    errors = res.get("errors")
                                    if errors:
                                        print()

                            break

            # Cleanup tmp directory after processing each zip file
            shutil.rmtree(tmp_dir)
            os.makedirs(tmp_dir)  # Recreate for the next iteration


def optimize_model(voice_model, gradio_server_port):
    create_voice_model_config = Operations.mutation.create_voice_model_config
    # Optimize model parameters
    study = optuna.create_study(direction="maximize")
    voice_model_sha256_hash = voice_model["checksumSHA256ForWeights"]
    model_weight_filename = f"{voice_model_sha256_hash}.pth"
    model_index_path = f"shared/logs/{voice_model_sha256_hash}.index"

    gender = voice_model["sourceModel"]["inferredProfile"]["gender"]

    gradio_server_url = f"http://localhost:{gradio_server_port}/"

    study.optimize(
        lambda trial: objective(
            trial,
            gradio_server_url,
            model_weight_filename,
            model_index_path,
            gender,
        ),
        n_trials=OPTIMIZATION_TRIAL_COUNT,
        show_progress_bar=OPTUNA_SHOW_PROGRESS_BAR,
    )

    input_data = {
        "qualityScore": study.best_value,
        "f0Curve": F0_CURVE,
        "transposePitch": TRANSPOSE_PITCH,
        "pitchExtractionMethod": PITCH_EXTRACTION_METHOD,
        "searchFeatureRatio": study.best_params["search_feature_ratio"],
        "filterRadius": study.best_params["filter_radius"],
        "audioResampling": AUDIO_RESAMPLING,
        "volumeEnvelopeScaling": study.best_params["volume_envelope_scaling"],
        "artifactProtection": study.best_params["artifact_protection"],
        "voiceModelId": voice_model["id"],
    }

    res = endpoint(query=create_voice_model_config, variables={"input": input_data})
    print(res["data"]["createVoiceModelConfig"])
    errors = res.get("errors")
    if errors:
        print(errors)


def process_voice_models(models, port):
    for model in tqdm(models):
        try:
            optimize_model(model, gradio_server_port=port)
        except Exception as e:
            error_message = str(e)
            model_info = json.dumps(model, default=str, indent=4)

            error_filename = f"errors/error_{model['id']}.txt"

            with open(error_filename, "w") as file:
                file.write(
                    f"Model Info:\n{model_info}\n\nError Message:\n{error_message}"
                )


def tune_voice_models_and_populate_voice_model_config_table(voice_model_dir):
    voice_models_query = Operations.query.voice_models
    page_end_cursor = None
    has_next_page = True

    voice_models = []

    while has_next_page:
        res = endpoint(query=voice_models_query, variables={"after": page_end_cursor})

        errors = res.get("errors")
        if errors:
            continue

        voice_model_connection = res["data"]["VoiceModels"]
        page_end_cursor = voice_model_connection["pageInfo"]["endCursor"]
        has_next_page = voice_model_connection["pageInfo"]["hasNextPage"]

        for edge in voice_model_connection["edges"]:
            voice_models.append(edge["node"])

    voice_model_configs_query = Operations.query.voice_model_configs
    page_end_cursor = None
    has_next_page = True

    voice_model_configs = []
    while has_next_page:
        res = endpoint(
            query=voice_model_configs_query, variables={"after": page_end_cursor}
        )

        errors = res.get("errors")
        if errors:
            continue

        voice_model_config_connection = res["data"]["VoiceModelConfigs"]
        page_end_cursor = voice_model_config_connection["pageInfo"]["endCursor"]
        has_next_page = voice_model_config_connection["pageInfo"]["hasNextPage"]

        for edge in voice_model_config_connection["edges"]:
            voice_model_configs.append(edge["node"])

    voice_models_filtered = [
        model
        for model in voice_models
        if model["id"] not in {config["voiceModelId"] for config in voice_model_configs}
    ]

    voice_model_chunks = list(chunk_it(voice_models_filtered, MAX_WORKER_THREADS))

    with ThreadPoolExecutor(max_workers=MAX_WORKER_THREADS) as executor:
        for i, models_chunk in enumerate(voice_model_chunks):
            port = GRADIO_SERVER_PORTS[i]
            executor.submit(process_voice_models, models_chunk, port)
        # print(results)


def main():
    # # sheet_data = get_sheet_json(doc_id, sheet_id)
    # sheet_data = json.load(open("./sheet.json"))
    # sheet_rows = get_sheet_rows(sheet_data)

    # populate_aihub_voice_model_and_voice_model_backup_url_tables(sheet_rows)
    # generate_voice_model_profiles_with_openai(VOICE_MODEL_PROFILES_OUTPUT_DIR)
    # populate_voice_model_profile_table(VOICE_MODEL_PROFILES_OUTPUT_DIR)
    # download_voice_model_weights(VOICE_MODEL_WEIGHTS_OUTPUT_DIR)
    # populate_voice_model_table_and_build_weights_folder_structure(
    #     VOICE_MODEL_WEIGHTS_OUTPUT_DIR, VOICE_MODEL_SHARED_DIR
    # )
    tune_voice_models_and_populate_voice_model_config_table(VOICE_MODEL_SHARED_DIR)


if __name__ == "__main__":
    main()
