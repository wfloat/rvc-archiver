# Compute average frequency of the base male and female voices

import numpy as np
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import cv2
import random
import os
import math
import sys
from sgqlc.endpoint.http import HTTPEndpoint
from graphql.generated.operations import Operations
from dotenv import load_dotenv

load_dotenv()

SILENCE_THRESHOLD = 10  # in hundredths of a second
SEGMENT_MINIMUM_LENGTH = 100  # in hundredths of a second
SEGMENT_FRAMES_SAMPLING_WIDTH = 75  # in hundredths of a second
SEGMENT_FRAMES_COUNT = 4  # Amount of frames to pull from the video for each sample
SEGMENT_RANDOM_SELECTION_COUNT = 20

F0_SAMPLE_RATE = 100  # HZ

WFLOAT_API_URL = os.getenv("WFLOAT_API_URL")
WFLOAT_API_KEY = os.getenv("WFLOAT_API_KEY")

headers = {
    "authorization": WFLOAT_API_KEY,
}
endpoint = HTTPEndpoint(WFLOAT_API_URL, headers)


@dataclass
class SpeechSegment:
    index_start: int
    index_end: int


def get_voice_models():
    voice_models = []
    voice_models_query = Operations.query.voice_models
    page_end_cursor = None
    has_next_page = True

    while has_next_page:
        res = endpoint(query=voice_models_query, variables={"after": page_end_cursor})

        errors = res.get("errors")
        if errors:
            continue

        voice_model_connection = res["data"]["VoiceModels"]
        page_end_cursor = voice_model_connection["pageInfo"]["endCursor"]
        has_next_page = voice_model_connection["pageInfo"]["hasNextPage"]

        for edge in voice_model_connection["edges"]:
            if edge["node"]["hidden"] == False:
                voice_models.append(edge["node"])

    page_end_cursor = None
    has_next_page = True

    return voice_models


def duration_str_to_seconds(duration_str: str) -> int:
    """
    Converts a length string in the format "HH:MM:SS" or "MM:SS" to the total number of seconds.

    Args:
    duration_str (str): A string representing a time duration in the format "HH:MM:SS" or "MM:SS".

    Returns:
    int: Total number of seconds represented by the input string.
    """
    # Split the string into its components
    parts = duration_str.split(":")

    # Check the number of parts and calculate the total seconds accordingly
    if len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
        total_seconds = hours * 3600 + minutes * 60 + seconds
    elif len(parts) == 2:
        minutes, seconds = map(int, parts)
        total_seconds = minutes * 60 + seconds
    else:
        raise ValueError(
            "Invalid time duration format. Expected 'HH:MM:SS' or 'MM:SS'."
        )

    return total_seconds


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


def compute_f0_from_segment(input_path: str, segment_start_time, segment_end_time):
    frequencies = read_file_to_numpy_array(input_path)
    start_index = segment_start_time * F0_SAMPLE_RATE
    end_index = segment_end_time * F0_SAMPLE_RATE
    segment_frequencies = frequencies[int(start_index) : int(end_index)]
    average = average_excluding_below_10(segment_frequencies)
    return average


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

    if len(sys.argv) != 4:
        print("Usage: script.py <VoiceModelId> <start time> <end time>")
        sys.exit(1)

    voice_model_id = sys.argv[1]
    print(voice_model_id)
    start_time_str = sys.argv[2]
    end_time_str = sys.argv[3]

    voice_models = get_voice_models()
    voice_model_matches = [obj for obj in voice_models if obj["id"] == voice_model_id]
    voice_model = voice_model_matches[0] if voice_model_matches else None

    try:
        start_time_seconds = duration_str_to_seconds(start_time_str)
        end_time_seconds = duration_str_to_seconds(end_time_str)
        print(
            f"start time (sec): {start_time_seconds}, end time (sec): {end_time_seconds}"
        )

        gender = voice_model["sourceModel"]["inferredProfile"]["gender"]
        f0_base = None
        if gender == "female":
            f0_base = female_f0
        else:
            f0_base = male_f0

        print(
            f"Voice Model id: {voice_model_id}, Start Time (seconds): {start_time_seconds}, End Time (seconds): {end_time_seconds}"
        )

        F0_SAMPLE_DIR = "frequency/f0"
        f0_voice_model = compute_f0_from_segment(
            f"{F0_SAMPLE_DIR}/{voice_model_id}.txt",
            start_time_seconds,
            end_time_seconds,
        )

        print(f"base f0: {f0_base}, new f0: {f0_voice_model}")
        pitch_shift = calculate_semitone_shift(f0_base, f0_voice_model)
        print(pitch_shift)

    except ValueError as e:
        print(e)
        sys.exit(1)

    print()


if __name__ == "__main__":
    main()
