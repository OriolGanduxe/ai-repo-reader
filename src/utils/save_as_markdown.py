import os
import re

def get_next_file_name(base_folder: str, base_name: str, extension: str) -> str:
    files = [f for f in os.listdir(base_folder) if f.startswith(base_name) and f.endswith(f".{extension}")]
    files.sort()

    if not files:
        counter = 1
    else:
        last_file = files[-1]
        counter = int(re.search(r'\d+', last_file).group()) + 1

    return f"{base_folder}/{base_name}{counter:03d}.{extension}"

def save_as_markdown(text: str, base_folder: str = "output", base_name: str = "001", extension: str = "md"):
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    file_name = get_next_file_name(base_folder, base_name, extension)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text)