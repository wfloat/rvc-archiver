# Seed the database with new data from https://docs.google.com/spreadsheets/d/1leF7_c2Qf5iQRVkmOF51ZSynOvEjz8fHqwriX1wUMPw/edit#gid=537336172
import os
import json
import requests
import optuna

# from util.google_sheet import get_sheet_rows

# from graphql.generated.operations import mutation_create_aihub_voice_model

from graphql.generated.schema import CreateAIHubVoiceModelInput
from graphql.generated.operations import Operations
from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint

endpoint = HTTPEndpoint("http://localhost:4000")

# input = CreateAIHubVoiceModelInput()
input.download_count = 0

create_aihub_voice_model2 = Operations.mutation.create_aihub_voice_model2

input_data = {
    "downloadCount": 100,
    "filename": "testfile",
    "version": "RVC v2",
}

op = Operation(create_aihub_voice_model2)
op.create_aihub_voice_model(input)

res = endpoint(query=create_aihub_voice_model2, variables={"input": input_data})
errors = res.get("errors")
data = create_aihub_voice_model2 + res
ans = data.create_aihub_voice_model2
if errors:
    raise SystemExit(errors)

print(res)


# VIDEO_LENGTH_MINIMUM = 240


# def main():
#     # Load model metadata from spreadsheet
#     doc_id = os.environ.get("DOC_ID")
#     sheet_id = os.environ.get("SHEET_ID")

#     # sheet_data = get_sheet_json(doc_id, sheet_id)
#     sheet_data = json.load(open("./sheet.json"))

#     sheet_rows = get_sheet_rows(sheet_data)

#     input = CreateAIHubVoiceModelInput(input={})

#     for sheet_row in sheet_rows:
#         print(sheet_row)
#         operation = mutation_create_aihub_voice_model()

#         continue


# if __name__ == "__main__":
#     main()
