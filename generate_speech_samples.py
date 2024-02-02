import os
import requests
from tqdm import tqdm

MALE_VOICE = "Andrew"
FEMALE_VOICE = "Ava"

TEXT_TO_SPEECH_URL = "http://localhost:5379"
TEXT_TO_SPEECH_ENDPOINT = f"{TEXT_TO_SPEECH_URL}/text_to_speech"

SPEECH_SAMPLE_DIR = "shared/input"


def generate_speech_samples():
    speeches = [
        "The quick brown fox jumps over the lazy dog.",
        "Where do bright violets bloom in relation to ancient oaks?",
        "Complex systems evolve from simple rules.",
        "Thunderstorms could delay the early morning flight.",
        "A murmuration of starlings filled the dusky sky.",
        "She sells seashells by the seashore.",
        "The mysterious manuscript contained unfamiliar symbols.",
        "Artificial intelligence transforms industries globally.",
        "What type of melody did the jazz saxophonist play?",
        "Climate change affects global weather patterns.",
        "Quantum computing revolutionizes data processing, offering solutions to previously unsolvable problems.",
        "Digital encryption secures online transactions, right?",
        "Ancient civilizations crafted remarkable artifacts.",
        "The culinary artist designed a five-course meal.",
        "How do renewable energy sources impact carbon emissions?",
        "Theoretical physics explores multidimensional spaces.",
        "Quantum computing revolutionizes data processing.",
        "The ancient library contained manuscripts that chronicled the lost civilization's history and knowledge.",
        "Bioluminescent creatures light up the ocean depths.",
        "The geneticist decoded the DNA sequence efficiently.",
    ]

    male_voice_lowercase = MALE_VOICE.lower()
    male_output_dir = os.path.join(SPEECH_SAMPLE_DIR, male_voice_lowercase)

    female_voice_lowercase = FEMALE_VOICE.lower()
    female_output_dir = os.path.join(SPEECH_SAMPLE_DIR, female_voice_lowercase)
    os.makedirs(male_output_dir, exist_ok=True)
    os.makedirs(female_output_dir, exist_ok=True)

    for index, speech in tqdm(enumerate(speeches)):
        body = {"voice": MALE_VOICE, "inputText": speech}

        response = requests.post(TEXT_TO_SPEECH_ENDPOINT, json=body)
        file_path = os.path.join(male_output_dir, f"{index}.wav")
        with open(file_path, "wb") as f:
            f.write(response.content)

    for index, speech in tqdm(enumerate(speeches)):
        body = {"voice": FEMALE_VOICE, "inputText": speech}

        response = requests.post(TEXT_TO_SPEECH_ENDPOINT, json=body)
        file_path = os.path.join(female_output_dir, f"{index}.wav")
        with open(file_path, "wb") as f:
            f.write(response.content)


if __name__ == "__main__":
    generate_speech_samples()
