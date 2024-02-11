# Marks some VoiceModels hidden = False based on voices.csv
import pandas as pd
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

WFLOAT_API_URL = os.getenv("WFLOAT_API_URL")


endpoint = HTTPEndpoint(WFLOAT_API_URL)
update_voice_model = Operations.mutation.update_voice_model
# Load the CSV file
df = pd.read_csv("voices.csv")

# Iterate over each row
for index, row in df.iterrows():
    id_value = row["ID"]
    hidden_value = row["HIDDEN"]

    res = endpoint(
        query=update_voice_model,
        variables={
            "input": {
                "id": id_value,
                "hidden": hidden_value,
            }
        },
    )
