import os
import json

directory = "profiles"  # Replace with your directory path
matching_files_count = 0
total_files = 0

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        total_files += 1
        with open(os.path.join(directory, filename), "r") as file:
            data = json.load(file)
            native_language = data.get("nativeLanguage")
            if (
                data.get("name") is not None
                and native_language is not None
                and native_language.lower() == "english"
            ):
                matching_files_count += 1

percentage = (matching_files_count / total_files) * 100 if total_files > 0 else 0
print(
    f"Percentage of JSON files with non-null 'name' and 'nativeLanguage' equal to 'English': {percentage}%"
)
