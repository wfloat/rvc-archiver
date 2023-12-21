from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import requests
import json

@dataclass
class AiHubSheetRow:
    url: Optional[str]
    download_counter: Optional[int]
    model_name: Optional[str]
    filename: Optional[str]
    file_size: Optional[int]
    md5_hash: Optional[str]
    rvc_version: Optional[str]
    alt_url1: Optional[str]
    alt_url2: Optional[str]
    alt_url3: Optional[str]
    alt_url4: Optional[str]
    alt_url5: Optional[str]
    alt_url6: Optional[str]
    alt_url7: Optional[str]
    alt_url8: Optional[str]
    alt_url9: Optional[str]
    alt_url10: Optional[str]
    alt_url11: Optional[str]
    alt_url12: Optional[str]
    alt_url13: Optional[str]
    alt_url14: Optional[str]
    alt_url15: Optional[str]
    alt_url16: Optional[str]
    alt_url17: Optional[str]
    alt_url18: Optional[str]
    alt_url19: Optional[str]

def get_sheet_json(doc_id: str, sheet_id: str) -> Dict[str, Any]:
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

def get_sheet_rows(data: Dict[str, Any]) -> List[AiHubSheetRow]:
    rows = data['table']['rows']
    sheet_rows: List[AiHubSheetRow] = []
    for row in rows:
        cells = row['c']
        ai_hub_sheet_row = AiHubSheetRow(
            url = cells[0]['v'] if cells[0] is not None else None,
            download_counter = cells[1]['v'] if cells[1] is not None else None,
            model_name = cells[2]['v'] if cells[2] is not None else None,
            filename = cells[3]['v'] if cells[3] is not None else None,
            file_size = cells[4]['v'] if cells[4] is not None else None,
            md5_hash = cells[5]['v'] if cells[5] is not None else None,
            rvc_version = cells[6]['v'] if cells[6] is not None else None,
            alt_url1 = cells[7]['v'] if cells[7] is not None else None,
            alt_url2 = cells[8]['v'] if cells[8] is not None else None,
            alt_url3 = cells[9]['v'] if cells[9] is not None else None,
            alt_url4 = cells[10]['v'] if cells[10] is not None else None,
            alt_url5 = cells[11]['v'] if cells[11] is not None else None,
            alt_url6 = cells[12]['v'] if cells[12] is not None else None,
            alt_url7 = cells[13]['v'] if cells[13] is not None else None,
            alt_url8 = cells[14]['v'] if cells[14] is not None else None,
            alt_url9 = cells[15]['v'] if cells[15] is not None else None,
            alt_url10 = cells[16]['v'] if cells[16] is not None else None,
            alt_url11 = cells[17]['v'] if cells[17] is not None else None,
            alt_url12 = cells[18]['v'] if cells[18] is not None else None,
            alt_url13 = cells[19]['v'] if cells[19] is not None else None,
            alt_url14 = cells[20]['v'] if cells[20] is not None else None,
            alt_url15 = cells[21]['v'] if cells[21] is not None else None,
            alt_url16 = cells[22]['v'] if cells[22] is not None else None,
            alt_url17 = cells[23]['v'] if cells[23] is not None else None,
            alt_url18 = cells[24]['v'] if cells[24] is not None else None,
            alt_url19 = cells[25]['v'] if cells[25] is not None else None,
        )
        sheet_rows.append(ai_hub_sheet_row)

    return sheet_rows

def get_first_row_as_ai_hub_sheet_row(data):
    first_row = data['table']['rows'][0]['c']

    return AiHubSheetRow(
        url=first_row[0]['v'],
        download_counter=first_row[1]['v'],
        model_name=first_row[2]['v'],
        filename=first_row[3]['v'],
        file_size=first_row[4]['v'],
        md5_hash=first_row[5]['v'],
        rvc_version=first_row[6]['v'],
        alt_url1 = first_row[7]['v'],
        alt_url2 = first_row[8]['v'],
        alt_url3 = first_row[9]['v'],
        alt_url4 = first_row[10]['v'],
        alt_url5 = first_row[11]['v'],
        alt_url6 = first_row[12]['v'],
        alt_url7 = first_row[13]['v'],
        alt_url8 = first_row[14]['v'],
        alt_url9 = first_row[15]['v'],
        alt_url10 = first_row[16]['v'],
        alt_url11 = first_row[17]['v'],
        alt_url12 = first_row[18]['v'],
        alt_url13 = first_row[19]['v'],
        alt_url14 = first_row[20]['v'],
        alt_url15 = first_row[21]['v'],
        alt_url16 = first_row[22]['v'],
        alt_url17 = first_row[23]['v'],
        alt_url18 = first_row[24]['v'],
        alt_url19 = first_row[25]['v'],
    )
