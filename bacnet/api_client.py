import json
import requests


def fetch_objects(from_type, path=None):
    """
    Function for fetching objects in file or in api
    :param from_type: source of objects (file or api)
    :param path: path to file or api
    """
    if from_type == "file":
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        response = requests.get(path)
        response.raise_for_status()
        return response.json()