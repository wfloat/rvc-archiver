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
- Store stat sheet data
- Label the stat sheet data and infer the character/person with OpenAI
- Pull video(s) that are compiled quality audio samples of the character
- Run F0 on the video's audio with RMVPE✅
- Remove background noise from audio
- Split the audio F0s into frequency segments✅
- Extract frame segments from the video that correspond to the respective audio frequency segment✅
- Show some of the frame segments to OpenAI and have it guess if the character/person we want is speaking
- Compute the average F0 on the validated audio segments
- Use the averaged F0 for optimizing the RVC model params
- Tune RVC model with Optuna set at the derived pitch transpose✅
- Store the character/person info with the correct RVC params to use for inference