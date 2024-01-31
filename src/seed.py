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

load_dotenv()


# Load model metadata from spreadsheet
GOOGLE_DOC_ID = os.environ.get("DOC_ID")
GOOGLE_SHEET_ID = os.environ.get("SHEET_ID")

WFLOAT_API_URL = os.getenv("WFLOAT_API_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

VOICE_MODEL_PROFILES_OUTPUT_PATH = "profiles"

endpoint = HTTPEndpoint(WFLOAT_API_URL)


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


def populate_tables_aihub_voice_model_and_voice_model_backup_url(
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


def generate_voice_model_profiles_with_openai(output_path: str):
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
        voice_profile_path = f"{output_path}/{md5_hash}.json"
        with open(voice_profile_path, "w") as file:
            json.dump(response, file)


def main():
    # sheet_data = get_sheet_json(doc_id, sheet_id)
    sheet_data = json.load(open("./sheet.json"))
    sheet_rows = get_sheet_rows(sheet_data)

    populate_tables_aihub_voice_model_and_voice_model_backup_url(sheet_rows)
    generate_voice_model_profiles_with_openai(VOICE_MODEL_PROFILES_OUTPUT_PATH)


if __name__ == "__main__":
    main()
