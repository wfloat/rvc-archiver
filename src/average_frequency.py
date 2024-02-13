# Compute average frequency of the base male and female voices

import numpy as np
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import cv2
import random
import os

SILENCE_THRESHOLD = 10  # in hundredths of a second
SEGMENT_MINIMUM_LENGTH = 100  # in hundredths of a second
SEGMENT_FRAMES_SAMPLING_WIDTH = 75  # in hundredths of a second
SEGMENT_FRAMES_COUNT = 4  # Amount of frames to pull from the video for each sample
SEGMENT_RANDOM_SELECTION_COUNT = 20


@dataclass
class SpeechSegment:
    index_start: int
    index_end: int


def read_file_to_numpy_array(file_path: str) -> List[float]:
    with open(file_path, "r") as file:
        array = np.array([float(line.strip()) for line in file])
    return array


def segment_speech_audio(frequencies: List[float]) -> list[SpeechSegment]:
    segments: list[SpeechSegment] = []
    segment_index_start = None
    segment_index_end = None
    silence_length = 0

    for index, frequency in enumerate(frequencies):
        if frequency == 0:
            silence_length = silence_length + 1

            if silence_length > SILENCE_THRESHOLD:
                if segment_index_end != None:
                    segments.append(
                        SpeechSegment(
                            index_start=segment_index_start, index_end=segment_index_end
                        )
                    )
                    segment_index_start = None
                    segment_index_end = None

        else:
            silence_length = 0

            if segment_index_start == None:
                segment_index_start = index
                segment_index_end = index
            else:
                segment_index_end = index

    segments_filtered = []
    for segment in segments:
        if segment.index_end - segment.index_start > SEGMENT_MINIMUM_LENGTH:
            segments_filtered.append(segment)

    return segments_filtered


# def save_video_frames(
#     SpeechSegment: SpeechSegment,
#     frequencies_count: int,
#     video_capture,
#     video_total_frames: int,
#     output_dir: str,
# ):
#     segment_index_start = SpeechSegment.index_start
#     segment_index_end = SpeechSegment.index_end

#     segment_midpoint = (segment_index_start + segment_index_end) / 2.0
#     frame_sampling_start = segment_midpoint - SEGMENT_FRAMES_SAMPLING_WIDTH / 2
#     frame_sampling_end = segment_midpoint + SEGMENT_FRAMES_SAMPLING_WIDTH / 2

#     frame_sampling_positions = np.linspace(
#         frame_sampling_start, frame_sampling_end, num=SEGMENT_FRAMES_COUNT
#     )

#     for index, frame_sampling_position in enumerate(frame_sampling_positions):
#         frame_position_normalized = frame_sampling_position / frequencies_count

#         audio_frame_index = int(frame_sampling_position)

#         frame_index = int(frame_position_normalized * video_total_frames)
#         video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
#         ret, frame = video_capture.read()
#         if ret:
#             frame_filename = f"{output_dir}/{audio_frame_index}.jpg"
#             cv2.imwrite(frame_filename, frame)
#             print(f"Saved {frame_filename}")
#         else:
#             print(f"Error reading frame at position {audio_frame_index}")


FEMALE_OUTPUT_DIR = "frequency/ava"
MALE_OUTPUT_DIR = "frequency/andrew"


def main():
    input_dir = MALE_OUTPUT_DIR
    f0_files = [file for file in os.listdir(input_dir) if file.endswith(".txt")]
    for file in f0_files:
        frequencies = read_file_to_numpy_array(f"{input_dir}/{file}")
        frequencies_count = len(frequencies)
        segments = segment_speech_audio(frequencies)
        print()


if __name__ == "__main__":
    main()
