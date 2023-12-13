# Utilities for parsing the AIHub RealtimeRVCStats spreadsheet at https://docs.google.com/spreadsheets/d/1leF7_c2Qf5iQRVkmOF51ZSynOvEjz8fHqwriX1wUMPw/edit#gid=537336172 
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import requests
import json

@dataclass
class AIHubSheetRow:
    url: Optional[str]
    downloadCounter: Optional[int]
    modelName: Optional[str]
    filename: Optional[str]
    fileSize: Optional[int]
    md5Hash: Optional[str]
    rvcVersion: Optional[str]
    altUrl1: Optional[str]
    altUrl2: Optional[str]
    altUrl3: Optional[str]
    altUrl4: Optional[str]
    altUrl5: Optional[str]
    altUrl6: Optional[str]
    altUrl7: Optional[str]
    altUrl8: Optional[str]
    altUrl9: Optional[str]
    altUrl10: Optional[str]
    altUrl11: Optional[str]
    altUrl12: Optional[str]
    altUrl13: Optional[str]
    altUrl14: Optional[str]
    altUrl15: Optional[str]
    altUrl16: Optional[str]
    altUrl17: Optional[str]
    altUrl18: Optional[str]
    altUrl19: Optional[str]

def get_sheet_json(doc_id: str, sheet_id: str)-> Dict[str, Any]:
    format = "json"
    url = f"https://docs.google.com/spreadsheets/d/{doc_id}/gviz/tq?tqx=out:{format}&tq&gid={sheet_id}"
    print(f"Downloading Google sheet at {url}")
    response = requests.get(url)
    result = response.text

    # Cleaning up the response
    start_to_remove = "/*O_o*/\ngoogle.visualization.Query.setResponse("
    end_to_remove = ");"
    result = result[len(start_to_remove):]
    result = result[:-len(end_to_remove)]
    
    return json.loads(result)

def get_sheet_rows(data: Dict[str, Any]) -> List[AIHubSheetRow]:
    rows = data['table']['rows']
    sheet_rows: List[AIHubSheetRow] = []
    for row in rows:
        cells = row['c']
        ai_hub_sheet_row = AIHubSheetRow(
            url = cells[0]['v'] if cells[0] is not None else None,
            downloadCounter = cells[1]['v'] if cells[1] is not None else None,
            modelName = cells[2]['v'] if cells[2] is not None else None,
            filename = cells[3]['v'] if cells[3] is not None else None,
            fileSize = cells[4]['v'] if cells[4] is not None else None,
            md5Hash = cells[5]['v'] if cells[5] is not None else None,
            rvcVersion = cells[6]['v'] if cells[6] is not None else None,
            altUrl1 = cells[7]['v'] if cells[7] is not None else None,
            altUrl2 = cells[8]['v'] if cells[8] is not None else None,
            altUrl3 = cells[9]['v'] if cells[9] is not None else None,
            altUrl4 = cells[10]['v'] if cells[10] is not None else None,
            altUrl5 = cells[11]['v'] if cells[11] is not None else None,
            altUrl6 = cells[12]['v'] if cells[12] is not None else None,
            altUrl7 = cells[13]['v'] if cells[13] is not None else None,
            altUrl8 = cells[14]['v'] if cells[14] is not None else None,
            altUrl9 = cells[15]['v'] if cells[15] is not None else None,
            altUrl10 = cells[16]['v'] if cells[16] is not None else None,
            altUrl11 = cells[17]['v'] if cells[17] is not None else None,
            altUrl12 = cells[18]['v'] if cells[18] is not None else None,
            altUrl13 = cells[19]['v'] if cells[19] is not None else None,
            altUrl14 = cells[20]['v'] if cells[20] is not None else None,
            altUrl15 = cells[21]['v'] if cells[21] is not None else None,
            altUrl16 = cells[22]['v'] if cells[22] is not None else None,
            altUrl17 = cells[23]['v'] if cells[23] is not None else None,
            altUrl18 = cells[24]['v'] if cells[24] is not None else None,
            altUrl19 = cells[25]['v'] if cells[25] is not None else None,
        )
        sheet_rows.append(ai_hub_sheet_row)

    return sheet_rows

def get_first_row_as_ai_hub_sheet_row(data):
    firstRow = data['table']['rows'][0]['c']

    return AIHubSheetRow(
        url=firstRow[0]['v'],
        downloadCounter=firstRow[1]['v'],
        modelName=firstRow[2]['v'],
        filename=firstRow[3]['v'],
        fileSize=firstRow[4]['v'],
        md5Hash=firstRow[5]['v'],
        rvcVersion=firstRow[6]['v'],
        altUrl1 = firstRow[7]['v'],
        altUrl2 = firstRow[8]['v'],
        altUrl3 = firstRow[9]['v'],
        altUrl4 = firstRow[10]['v'],
        altUrl5 = firstRow[11]['v'],
        altUrl6 = firstRow[12]['v'],
        altUrl7 = firstRow[13]['v'],
        altUrl8 = firstRow[14]['v'],
        altUrl9 = firstRow[15]['v'],
        altUrl10 = firstRow[16]['v'],
        altUrl11 = firstRow[17]['v'],
        altUrl12 = firstRow[18]['v'],
        altUrl13 = firstRow[19]['v'],
        altUrl14 = firstRow[20]['v'],
        altUrl15 = firstRow[21]['v'],
        altUrl16 = firstRow[22]['v'],
        altUrl17 = firstRow[23]['v'],
        altUrl18 = firstRow[24]['v'],
        altUrl19 = firstRow[25]['v'],
    )
 