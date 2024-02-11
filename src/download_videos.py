from pytube import YouTube, Search
from dataclasses import dataclass
from typing import Optional, List, Dict, Any


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
import time
import random
from tqdm import tqdm
import math

WFLOAT_API_URL = os.getenv("WFLOAT_API_URL")


endpoint = HTTPEndpoint(WFLOAT_API_URL)
update_voice_model = Operations.mutation.update_voice_model
# Load the CSV file
df = pd.read_csv("voices.csv")

# Iterate over each row
for index, row in tqdm(df.iterrows()):
    id_value = row["ID"]
    url_value = row["URL"]
    if not isinstance(url_value, str) and math.isnan(url_value):
        continue

    yt = YouTube(url_value)

    stream = yt.streams.get_lowest_resolution()
    stream.download(filename=f"videos/{id_value}.mp4")

    wait_time = random.randint(1, 5)
    time.sleep(wait_time)
