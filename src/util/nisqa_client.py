from typing import Optional, Literal
from dataclasses import dataclass, asdict
import requests

NISQA_PORT = 5240
NISQA_URL = f"http://localhost:{NISQA_PORT}"

pretrained_model_options = Literal["nisqa", "nisqa_mos_only", "nisqa_tts"]


@dataclass
class PredictFileArgs:
    pretrained_model: pretrained_model_options
    deg: str


@dataclass
class PredictFileResponse:
    deg: str
    mos_pred: float
    model: str
    noi_pred: Optional[float] = None
    dis_pred: Optional[float] = None
    col_pred: Optional[float] = None
    loud_pred: Optional[float] = None


def predict_speech_quality(args: PredictFileArgs) -> PredictFileResponse:
    endpoint = "predict_file"
    url = f"{NISQA_URL}/{endpoint}"
    headers = {"Content-Type": "application/json"}
    args_dict = asdict(args)

    response = requests.post(url, json=args_dict, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        return PredictFileResponse(**response_data)
    else:
        raise Exception(
            f"NISQA {endpoint} failed with status code: {response.status_code}"
        )
