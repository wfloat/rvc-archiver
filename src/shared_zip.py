# Builds the shared.zip with the VoiceModels have hidden = False
import os
import zipfile
from dotenv import load_dotenv
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from graphql.generated.schema import CreateAIHubVoiceModelInput
from graphql.generated.operations import Operations
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
import zipfile
from tqdm import tqdm

# Define the array of objects with criteria for including files in the ZIP
voice_models = []


def file_should_be_included(folder, filename):
    if folder == "weights" or folder == "logs":
        filename_without_extension, extension = os.path.splitext(filename)
        for voice_model in voice_models:
            if voice_model["checksumSHA256ForWeights"] == filename_without_extension:
                return True
    return False


specific_files_to_include = [
    "shared/f0/f0G40k.pth",
    "shared/f0/f0G48k.pth",
]

WFLOAT_API_URL = os.getenv("WFLOAT_API_URL")


endpoint = HTTPEndpoint(WFLOAT_API_URL)


def get_voice_models():
    voice_models_query = Operations.query.voice_models
    page_end_cursor = None
    has_next_page = True

    while has_next_page:
        res = endpoint(query=voice_models_query, variables={"after": page_end_cursor})

        errors = res.get("errors")
        if errors:
            continue

        voice_model_connection = res["data"]["VoiceModels"]
        page_end_cursor = voice_model_connection["pageInfo"]["endCursor"]
        has_next_page = voice_model_connection["pageInfo"]["hasNextPage"]

        for edge in voice_model_connection["edges"]:
            if edge["node"]["hidden"] == False:
                voice_models.append(edge["node"])

    page_end_cursor = None
    has_next_page = True

    return voice_models


# Create a ZIP file
with zipfile.ZipFile("shared.zip", "w", compression=zipfile.ZIP_DEFLATED) as myzip:
    get_voice_models()

    myzip.writestr("shared/input/", "")
    myzip.writestr("shared/output/", "")

    for folder_name, subfolders, filenames in os.walk("shared"):
        for filename in tqdm(filenames):
            if file_should_be_included(os.path.basename(folder_name), filename):
                file_path = os.path.join(folder_name, filename)
                # arcname = os.path.relpath(file_path, "shared")
                myzip.write(file_path, arcname=file_path)

print("ZIP file created successfully.")
