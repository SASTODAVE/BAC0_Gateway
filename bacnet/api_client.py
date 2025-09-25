import json

import requests

def values_from_api():
    response = requests.get(f"/objects/values")
    response.raise_for_status()
    return response.json()

def fetch_objects(from_type="file"):
    if from_type == "file":
        with open("lib/consommation_30minutes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        response = requests.get(f"objects")
        response.raise_for_status()
        return response.json()