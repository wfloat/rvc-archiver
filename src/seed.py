# Seed the database with new data from https://docs.google.com/spreadsheets/d/1leF7_c2Qf5iQRVkmOF51ZSynOvEjz8fHqwriX1wUMPw/edit#gid=537336172
import os
import json
from tqdm import tqdm
from dotenv import load_dotenv
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from graphql.generated.schema import CreateAIHubVoiceModelInput
from graphql.generated.operations import Operations
from util.google_sheet import get_sheet_rows
from urllib.parse import urlparse, urlunparse


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

endpoint = HTTPEndpoint(WFLOAT_API_URL)

# VIDEO_LENGTH_MINIMUM = 240


def main():
    # Load model metadata from spreadsheet
    doc_id = os.environ.get("DOC_ID")
    sheet_id = os.environ.get("SHEET_ID")

    # sheet_data = get_sheet_json(doc_id, sheet_id)
    sheet_data = json.load(open("./sheet.json"))
    sheet_rows = get_sheet_rows(sheet_data)

    create_aihub_voice_model = Operations.mutation.create_aihub_voice_model

    create_voice_model_backup_url = Operations.mutation.create_voice_model_backup_url

    for sheet_row in tqdm(sheet_rows):
        if sheet_row.rvc_version != "RVC v2":
            continue

        filename = remove_carriage_returns(sheet_row.filename)
        model_name = remove_carriage_returns(sheet_row.model_name)
        input_data = {
            "downloadCount": sheet_row.download_counter,
            "filename": filename,
            "name": model_name,
            "version": sheet_row.rvc_version,
            # "creatorText": # TODO: pull in creatorText from the "Oranized Model List w/ Credits" spreadsheet
        }

        res = endpoint(query=create_aihub_voice_model, variables={"input": input_data})
        errors = res.get("errors")
        # if errors:
        #     print(errors)

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
            # print(errors)

        else:
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


if __name__ == "__main__":
    main()
