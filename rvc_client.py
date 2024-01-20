from gradio_client import Client

# client = Client("http://localhost:7865/")
# result = client.predict(
# 				0,	# float (numeric value between 0 and 2333) in 'Select Speaker/Singer ID:' Slider component
# 				"Howdy!",	# str  in 'Enter the path of the audio folder to be processed (copy it from the address bar of the file manager):' Textbox component
# 				"Howdy!",	# str  in 'Specify output folder:' Textbox component
# 				["https://github.com/gradio-app/gradio/raw/main/test/test_files/sample_file.pdf"],	# List[str] (List of filepath(s) or URL(s) to files) in 'Multiple audio files can also be imported. If a folder path exists, this input is ignored.' File component
# 				5,	# float  in 'Transpose (integer, number of semitones, raise by an octave: 12, lower by an octave: -12):' Number component
# 				"pm",	# str  in 'Select the pitch extraction algorithm ('pm': faster extraction but lower-quality speech; 'harvest': better bass but extremely slow; 'crepe': better quality but GPU intensive), 'rmvpe': best quality, and little GPU requirement' Radio component
# 				"Howdy!",	# str  in 'Path to the feature index file. Leave blank to use the selected result from the dropdown:' Textbox component
# 				"logs/added_IVF163_Flat_nprobe_1_Omni-Man_MK1_v2.index",	# str (Option from: ['logs/added_IVF163_Flat_nprobe_1_Omni-Man_MK1_v2.index']) in 'Auto-detect index path and select from the dropdown:' Dropdown component
# 				0,	# float (numeric value between 0 and 1) in 'Search feature ratio (controls accent strength, too high has artifacting):' Slider component
# 				0,	# float (numeric value between 0 and 7) in 'If >=3: apply median filtering to the harvested pitch results. The value represents the filter radius and can reduce breathiness.' Slider component
# 				0,	# float (numeric value between 0 and 48000) in 'Resample the output audio in post-processing to the final sample rate. Set to 0 for no resampling:' Slider component
# 				0,	# float (numeric value between 0 and 1) in 'Adjust the volume envelope scaling. Closer to 0, the more it mimicks the volume of the original vocals. Can help mask noise and make volume sound more natural when set relatively low. Closer to 1 will be more of a consistently loud volume:' Slider component
# 				0,	# float (numeric value between 0 and 0.5) in 'Protect voiceless consonants and breath sounds to prevent artifacts such as tearing in electronic music. Set to 0.5 to disable. Decrease the value to increase protection, but it may reduce indexing accuracy:' Slider component
# 				"wav",	# str  in 'Export file format' Radio component
# 				api_name="/infer_convert_batch"
# )
# print(result)

# from gradio_client import Client

# client = Client("http://localhost:7865/")
# result = client.predict(
# 				api_name="/infer_refresh"
# )
# print(result)

# client = Client("http://localhost:7865/")
# result = client.predict(
# 				api_name="/infer_clean"
# )
# print(result)

client = Client("http://localhost:7865/", 
                output_dir="out"
        )

# result = client.predict(
# 				0,	# float (numeric value between 0 and 2333) in 'Select Speaker/Singer ID:' Slider component
# 				"./audio.wav",	# str  in 'Enter the path of the audio file to be processed (default is the correct format example):' Textbox component
# 				0,	# float  in 'Transpose (integer, number of semitones, raise by an octave: 12, lower by an octave: -12):' Number component
# 				None,	# str (filepath on your computer (or URL) of file) in 'F0 curve file (optional). One pitch per line. Replaces the default F0 and pitch modulation:' File component
# 				"harvest",	# str  in 'Select the pitch extraction algorithm ('pm': faster extraction but lower-quality speech; 'harvest': better bass but extremely slow; 'crepe': better quality but GPU intensive), 'rmvpe': best quality, and little GPU requirement' Radio component
# 				None,	# str  in 'Path to the feature index file. Leave blank to use the selected result from the dropdown:' Textbox component
# 				None,	# str (Option from: ['logs/added_IVF163_Flat_nprobe_1_Omni-Man_MK1_v2.index']) in 'Auto-detect index path and select from the dropdown:' Dropdown component
# 				0,	# float (numeric value between 0 and 1) in 'Search feature ratio (controls accent strength, too high has artifacting):' Slider component
# 				0,	# float (numeric value between 0 and 7) in 'If >=3: apply median filtering to the harvested pitch results. The value represents the filter radius and can reduce breathiness.' Slider component
# 				0,	# float (numeric value between 0 and 48000) in 'Resample the output audio in post-processing to the final sample rate. Set to 0 for no resampling:' Slider component
# 				0,	# float (numeric value between 0 and 1) in 'Adjust the volume envelope scaling. Closer to 0, the more it mimicks the volume of the original vocals. Can help mask noise and make volume sound more natural when set relatively low. Closer to 1 will be more of a consistently loud volume:' Slider component
# 				0,	# float (numeric value between 0 and 0.5) in 'Protect voiceless consonants and breath sounds to prevent artifacts such as tearing in electronic music. Set to 0.5 to disable. Decrease the value to increase protection, but it may reduce indexing accuracy:' Slider component
# 				api_name="/infer_convert"
# )


result = client.predict(
        "Omni-Man_MK1.pth",	# str (Option from: ['Omni-Man_MK1.pth']) in 'Inferencing voice:' Dropdown component
        0,	# float (numeric value between 0 and 0.5) in 'Protect voiceless consonants and breath sounds to prevent artifacts such as tearing in electronic music. Set to 0.5 to disable. Decrease the value to increase protection, but it may reduce indexing accuracy:' Slider component
        0,	# float (numeric value between 0 and 0.5) in 'Protect voiceless consonants and breath sounds to prevent artifacts such as tearing in electronic music. Set to 0.5 to disable. Decrease the value to increase protection, but it may reduce indexing accuracy:' Slider component
        api_name="/infer_change_voice"
)
result = client.predict(
        0,	# float (numeric value between 0 and 2333) in 'Select Speaker/Singer ID:' Slider component
        "shared/input/audio.wav",	# str  in 'Enter the path of the audio file to be processed (default is the correct format example):' Textbox component
        0,	# float  in 'Transpose (integer, number of semitones, raise by an octave: 12, lower by an octave: -12):' Number component
        "shared/f0/f0G40k.pth",	# str (filepath on your computer (or URL) of file) in 'F0 curve file (optional). One pitch per line. Replaces the default F0 and pitch modulation:' File component
        "harvest",	# str  in 'Select the pitch extraction algorithm ('pm': faster extraction but lower-quality speech; 'harvest': better bass but extremely slow; 'crepe': better quality but GPU intensive), 'rmvpe': best quality, and little GPU requirement' Radio component
        "shared/logs/added_IVF163_Flat_nprobe_1_Omni-Man_MK1_v2.index",	# str  in 'Path to the feature index file. Leave blank to use the selected result from the dropdown:' Textbox component
        "shared/logs/added_IVF163_Flat_nprobe_1_Omni-Man_MK1_v2.index",	# str (Option from: ['logs/added_IVF163_Flat_nprobe_1_Omni-Man_MK1_v2.index']) in 'Auto-detect index path and select from the dropdown:' Dropdown component
        0,	# float (numeric value between 0 and 1) in 'Search feature ratio (controls accent strength, too high has artifacting):' Slider component
        0,	# float (numeric value between 0 and 7) in 'If >=3: apply median filtering to the harvested pitch results. The value represents the filter radius and can reduce breathiness.' Slider component
        0,	# float (numeric value between 0 and 48000) in 'Resample the output audio in post-processing to the final sample rate. Set to 0 for no resampling:' Slider component
        0,	# float (numeric value between 0 and 1) in 'Adjust the volume envelope scaling. Closer to 0, the more it mimicks the volume of the original vocals. Can help mask noise and make volume sound more natural when set relatively low. Closer to 1 will be more of a consistently loud volume:' Slider component
        0,	# float (numeric value between 0 and 0.5) in 'Protect voiceless consonants and breath sounds to prevent artifacts such as tearing in electronic music. Set to 0.5 to disable. Decrease the value to increase protection, but it may reduce indexing accuracy:' Slider component
        api_name="/infer_convert"
)
print(result)
print(result)

# def typesafe_predict(
#     client,
#     speaker_id: float,
#     audio_path: str,
#     transpose: float, # raise by an octave: 12, lower by an octave: -12) not a ton
#     f0_curve_path: str, # At most 12 different ones
#     pitch_extraction: str, # At most 4 different ones
#     index_path: str, 
#     auto_detect_index_path: str, 
#     search_feature_ratio: float, #0.00 to 1.00 at most 100 step size 0.01
#     filter_radius: float, # 0-7 at most 7
#     resample_sr: float, # 0-48000 step size 1 (I think I keep this 0 for now)
#     rms_mix_rate: float, # 0.00 to 1.00 at most 100 step size 0.01
#     protect: float, # 0.00 to 0.50 at most 50 step size 0.01
#     api_name: str = "/infer_convert"
# ):