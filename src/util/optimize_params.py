from optuna import Trial
from gradio_client import Client
from util.rvc_client import infer_convert, InferenceParams


def objective(trial: Trial):
    params = InferenceParams(
        transpose_pitch = trial.suggest_int("transpose_pitch", -24, 24),
        pitch_extraction_method = trial.suggest_categorical("pitch_extraction_method", ("pm", "harvest", "crepe", "rmvpe")),
        search_feature_ratio = trial.suggest_float("search_feature_ratio", 0.0, 1.0, step=0.01),
        filter_radius = trial.suggest_int("filter_radius", 0, 7),
        audio_resampling = trial.suggest_int("audio_resampling", 0, 48000, step=1000),
        volume_envelope_scaling = trial.suggest_float("volume_envelope_scaling", 0.0, 1.0, step=0.01),
        artifact_protection = trial.suggest_float("artifact_protection", 0.0, 0.5, step=0.01),
    )

    gradio_server_url = "http://localhost:7865/"
    audio_input_file = "shared/input/audio.wav"
    audio_output_path = "shared/output"
    model_weight_filename = "Omni-Man_MK1.pth"
    model_index_path = "shared/logs/added_IVF163_Flat_nprobe_1_Omni-Man_MK1_v2.index"
    f0_curve_path = "shared/f0/f0G40k.pth"

    gradio_client = Client(gradio_server_url, output_dir=audio_output_path)

    audio_output_file = infer_convert(gradio_client, model_weight_filename, model_index_path, f0_curve_path, audio_input_file, params)
    print(audio_output_file)

    # TODO: Add NISQA
    return 0.5
