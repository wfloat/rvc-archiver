from optuna import Trial
from gradio_client import Client
from util.rvc_client import infer_convert, InferenceParams
from util.nisqa_client import PredictFileArgs, predict_speech_quality
from util.helpers import empty_directory
import os
import numpy as np
import shutil

TRANSPOSE_PITCH = 0
AUDIO_RESAMPLING = 0
PITCH_EXTRACTION_METHOD = "rmvpe"
F0_CURVE = "f0G40k.pth"


def objective(
    trial: Trial, gradio_server_url, model_weight_filename, model_index_path, gender
):
    # empty_directory("./shared/output")
    params = InferenceParams(
        # transpose_pitch = trial.suggest_int("transpose_pitch", -24, 24),
        # pitch_extraction_method = trial.suggest_categorical("pitch_extraction_method", ("pm", "harvest", "crepe", "rmvpe")),
        # search_feature_ratio = trial.suggest_float("search_feature_ratio", 0.0, 1.0, step=0.01),
        # filter_radius = trial.suggest_int("filter_radius", 0, 7),
        # audio_resampling = trial.suggest_int("audio_resampling", 0, 48000, step=1000),
        # volume_envelope_scaling = trial.suggest_float("volume_envelope_scaling", 0.0, 1.0, step=0.01),
        # artifact_protection = trial.suggest_float("artifact_protection", 0.0, 0.5, step=0.01),
        # transpose_pitch=trial.suggest_int("transpose_pitch", -24, 24),
        transpose_pitch=TRANSPOSE_PITCH,
        pitch_extraction_method=PITCH_EXTRACTION_METHOD,
        search_feature_ratio=trial.suggest_float(
            "search_feature_ratio", 0.0, 1.0, step=0.02
        ),  # 0.57,
        filter_radius=trial.suggest_int("filter_radius", 0, 7),  # 3,
        audio_resampling=AUDIO_RESAMPLING,
        volume_envelope_scaling=trial.suggest_float(
            "volume_envelope_scaling", 0.0, 1.0, step=0.02
        ),  # 0.41,
        artifact_protection=trial.suggest_float(
            "artifact_protection", 0.0, 0.5, step=0.02
        ),  # 0.08,
        # {'search_feature_ratio': 0.16, 'filter_radius': 3, 'volume_envelope_scaling': 0.14, 'artifact_protection': 0.1}
        # transpose_pitch = 0,
        # pitch_extraction_method = "rmvpe",
        # search_feature_ratio = 0.16,
        # filter_radius = 3,
        # audio_resampling = 0,
        # volume_envelope_scaling = 0.14,
        # artifact_protection = 0.1,
    )

    male_voice = "andrew"
    female_voice = "ava"
    audio_input_path = None
    if gender == "male":
        audio_input_path = os.path.join("shared/input", male_voice)
    else:
        audio_input_path = os.path.join("shared/input", female_voice)

    audio_output_path = "shared/output"
    f0_curve_path = f"shared/f0/{F0_CURVE}"

    gradio_client = Client(gradio_server_url, output_dir=audio_output_path)

    quality_scores = []
    audio_files = [f for f in os.listdir(audio_input_path) if f.endswith(".wav")]
    for audio_file in audio_files:
        audio_input_file = os.path.join(audio_input_path, audio_file)
        audio_output_file = infer_convert(
            gradio_client,
            model_weight_filename,
            model_index_path,
            f0_curve_path,
            audio_input_file,
            params,
        )

        quality_prediction_args = PredictFileArgs(
            pretrained_model="nisqa_tts", deg=audio_output_file
        )
        quality_response = predict_speech_quality(quality_prediction_args)
        quality = quality_response.mos_pred
        # print(quality, audio_output_file)

        quality_scores.append(quality)
        audio_output_dir = audio_output_file.replace(f"/audio.wav", "")
        shutil.rmtree(audio_output_dir)

    average_quality = np.mean(quality_scores)
    return average_quality
