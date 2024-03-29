import json
import os


def read_json(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)


def write_json(file_name: str, data):
    with open(file_name, "w") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )
