import os
import json
import requests
from util.google_sheet import get_sheet_json, get_sheet_rows

def main():
    # Environment variables
    doc_id = os.environ.get('DOC_ID')
    sheet_id = os.environ.get('SHEET_ID')

    # sheet_data = get_sheet_json(doc_id, sheet_id)
    sheet_data = json.load(open('./sheet.json'))

    sheet_rows = get_sheet_rows(sheet_data)
    print(sheet_rows)

main()
