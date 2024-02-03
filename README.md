# rvc-archiver

## Getting started

### Download F0 Transformation weights

```bash
curl -L -o shared/f0/D32k.pth      https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D32k.pth \
     -L -o shared/f0/D40k.pth      https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D40k.pth \
     -L -o shared/f0/D48k.pth      https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D48k.pth \
     -L -o shared/f0/G32k.pth      https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G32k.pth \
     -L -o shared/f0/G40k.pth      https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G40k.pth \
     -L -o shared/f0/G48k.pth      https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G48k.pth \
     -L -o shared/f0/f0D32k.pth    https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D32k.pth \
     -L -o shared/f0/f0D40k.pth    https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D40k.pth \
     -L -o shared/f0/f0D48k.pth    https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D48k.pth \
     -L -o shared/f0/f0G32k.pth    https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G32k.pth \
     -L -o shared/f0/f0G40k.pth    https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G40k.pth \
     -L -o shared/f0/f0G48k.pth    https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G48k.pth
```

### Code Generation

```bash
python3 src/graphql/codegen.py
```

## TODO:

- Add the f0 curve as an inference param for Optuna
- Try optimizing different RVC models
- Experiment with different Azure TTS models for each of the RVC models
  - I need to figure out if it is better to use the same voice for all the models or have different voices
  - I think this could be turned into a Optuna parameter or potentially Optuna has a way to look at multiple models in their Jupyter Notebook
  - Make f0 curve a parameter
- Pull all the model MD5 hashes that are already stored in the database

## Process

- Pull data from RVCStatSheet.csv✅
- Store stat sheet data✅
- Label the stat sheet data and infer the character/person with OpenAI✅
- Pull video(s) that are compiled quality audio samples of the character
- Run F0 on the video's audio with RMVPE✅
- Remove background noise from audio
- Split the audio F0s into frequency segments✅
- Extract frame segments from the video that correspond to the respective audio frequency segment✅
- Show some of the frame segments to OpenAI and have it guess if the character/person we want is speaking
- Compute the average F0 on the validated audio segments
- Use the averaged F0 for optimizing the RVC model params
- Tune RVC model with Optuna set at the derived pitch transpose✅
- Store the character/person info with the correct RVC params to use for inference✅

-- "06039080-116d-493e-87ab-6b219834a799" "7f3a561f-a167-4ac3-90db-8dd0147b28f8" 0.04 0 0 "rmvpe" 0.58 0 0.22 "f0G40k.pth" 3.63166352113088
-- "bcec0d61-9d30-4cdb-8ced-773c9b596108" "28b5807d-2f88-4950-ae19-8c71646d4034" 0.12 0 1 "rmvpe" 0.02 0 0.06 "f0G40k.pth" 3.960955540339152

TODO: Make the RVC container empty /tmp/gradio dir periodically to prevent size from growing indefinitely

temporary fix:

```bash
sudo -E python3 src/seed.py
# See around line 100 in optimize_params.py:
# if gradio_server_url == "http://localhost:7865/":
#     empty_directory("tmp-rvc-0")
# elif gradio_server_url == "http://localhost:7866/":
#     empty_directory("tmp-rvc-1")
# elif gradio_server_url == "http://localhost:7867/":
#     empty_directory("tmp-rvc-2")
```
