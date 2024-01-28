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


def remove_carriage_returns(input_str: str) -> str:
    if input_str is None:
        return ""
    return input_str.replace("\r", "")


load_dotenv()

WFLOAT_API_URL = os.getenv("WFLOAT_API_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

endpoint = HTTPEndpoint(WFLOAT_API_URL)


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

            input_data = {"url": url_standardized, "voiceModelId": model_id}
            res = endpoint(
                query=create_voice_model_backup_url, variables={"input": input_data}
            )
            errors = res.get("errors")
            if errors:
                print(errors)

        for i in range(1, 20):
            alt_url_field = f"alt_url{i}"
            alt_url_value = getattr(sheet_row, alt_url_field, None)

            if alt_url_value:
                alt_url_standardized = standardize_url(alt_url_value)

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


def main():
    # # Load model metadata from spreadsheet
    # doc_id = os.environ.get("DOC_ID")
    # sheet_id = os.environ.get("SHEET_ID")

    # # sheet_data = get_sheet_json(doc_id, sheet_id)
    # sheet_data = json.load(open("./sheet.json"))
    # sheet_rows = get_sheet_rows(sheet_data)

    # populate_tables_aihub_voice_model_and_voice_model_backup_url(sheet_rows)

    client = OpenAI()

    output_dir = "profiles"

    client = OpenAI(
        # This is the default and can be omitted
        api_key=OPENAI_API_KEY,
    )

    aihub_voice_models_query = Operations.query.aihub_voice_models
    page_end_cursor = None
    has_next_page = True
    i = 0

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
        print(i)
        i = i + 1

    print(page_end_cursor)

    # for sheet_row in tqdm(sheet_rows):

    # chat_completion = client.chat.completions.create(
    #     model="gpt-4-1106-preview",
    #     response_format={"type": "json_object"},
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "Given the following data VoiceModelData = { model_name: None, weights_name: 'MLP05RainbowDash', } I want you to make your best guess at filling in the following JSON of who this voice model represents. Note that the model name and weights name can contain meta data including but not limited to epochs/creation date/author name/dataset source that may or may not be directly useful to identifying who the voice model represents. The voice can be a fictional character or a real person. ProfileOrCharacter = { confidence: float # score 0.0 to 1.0 fameLevel: float # score 0.0 to 1.0 fictional: bool name: str gender: str # male or female relevantTags: str[] # if not None: minimum 5/maximum 10 accent: str nativeLanguage: str modelTrainedOnEnglishProbability: float } I need you to output only the filled in object",
    #         }
    #     ],
    # )

    # md5hash = "oiafonasfnalafeuia"

    # response = json.loads(chat_completion.choices[0].message.content)

    # voice_profile_path = f"{output_dir}/{md5hash}.json"
    # with open(voice_profile_path, "w") as file:
    #     json.dump(response, file)

    # print(response)


if __name__ == "__main__":
    main()
