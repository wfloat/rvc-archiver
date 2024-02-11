import csv
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
import os

WFLOAT_API_URL = os.getenv("WFLOAT_API_URL")


endpoint = HTTPEndpoint(WFLOAT_API_URL)


def get_voice_models():
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

    page_end_cursor = None
    has_next_page = True

    return voice_models


if __name__ == "__main__":
    voice_models = get_voice_models()

    # Specify the CSV file name
    csv_file = "voices.csv"

    # Write to the CSV file
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "ID", "PROCESSED", "HIDDEN"])  # Column headers
        for voice_model in voice_models:
            writer.writerow(
                [
                    voice_model["name"],
                    voice_model["id"],
                    voice_model["processed"],
                    voice_model["hidden"],
                ]
            )
