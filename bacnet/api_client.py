import json
import requests

def fetch_objects(from_type, path=None):
    if from_type == "file":
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        response = requests.get(path)
        response.raise_for_status()
        return response.json()