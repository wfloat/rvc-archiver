# Compute average frequency of the base male and female voices

import numpy as np
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import cv2
import random
import os
import math

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


FEMALE_OUTPUT_DIR = "frequency/ava"
MALE_OUTPUT_DIR = "frequency/andrew"


def average_excluding_below_10(arr):
    filtered_arr = arr[arr >= 10]  # Exclude elements below 10
    if filtered_arr.size == 0:
        return None  # Return None if no elements are >= 10
    return np.mean(filtered_arr)


def compute_f0(input_dir: str):
    f0_files = [file for file in os.listdir(input_dir) if file.endswith(".txt")]
    averages = []
    for file in f0_files:
        frequencies = read_file_to_numpy_array(f"{input_dir}/{file}")
        average = average_excluding_below_10(frequencies)
        averages.append(average)
    f0 = np.mean(averages)
    return f0
    print(f0)


def calculate_semitone_shift(f0_a, f0_b):
    """
    Parameters:
    - f0_a: The original frequency.
    - f0_b: The target frequency.
    """

    n = 12 * math.log2(f0_b / f0_a)
    return round(n)


def main():
    female_f0 = compute_f0(FEMALE_OUTPUT_DIR)
    male_f0 = compute_f0(MALE_OUTPUT_DIR)

    pitch_shift = calculate_semitone_shift(female_f0, male_f0)
    print()


if __name__ == "__main__":
    main()
