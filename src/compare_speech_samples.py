from util.nisqa_client import PredictFileArgs, predict_speech_quality

audio_file_a = "./shared/omniman_good.wav"
audio_file_b = "./shared/omniman_tuned_to_mario.wav"

quality_prediction_args = PredictFileArgs(
    pretrained_model="nisqa_tts",
    deg=audio_file_a
)

quality_response = predict_speech_quality(quality_prediction_args)
quality = quality_response.mos_pred
print(quality, audio_file_a)

quality_prediction_args = PredictFileArgs(
    pretrained_model="nisqa_tts",
    deg=audio_file_b
)

quality_response = predict_speech_quality(quality_prediction_args)
quality = quality_response.mos_pred
print(quality, audio_file_b)