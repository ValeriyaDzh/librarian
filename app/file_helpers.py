import json
import os


def load_data(file_path: str) -> dict:
    if os.path.exists(file_path):
        with open(file_path, encoding="utf-8") as file:
            return json.load(file)
    else:
        return {"books": []}


def save(data, file_path: str) -> None:
    existed_data = load_data(file_path)
    existed_data["books"].append(data)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(existed_data, file, ensure_ascii=False, indent=2)


def update(data, file_path: str) -> None:
    new_data = {"books": data}

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(new_data, file, ensure_ascii=False, indent=2)
