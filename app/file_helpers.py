import json
import os


def save(data, file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_data(file_path: str) -> list[str]:
    if os.path.exists(file_path):
        with open(file_path, encoding="utf-8") as file:
            return json.load(file)
    else:
        return []
