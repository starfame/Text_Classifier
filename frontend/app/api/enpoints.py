import io

import requests

from ..data import config


def get_labels(text):
    response = requests.post(config.ENDPOINT_ONE, json={"content": text})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Unexpected status code: {response.status_code}, Response: {response.text}")


def process_csv(file):
    response = requests.post(config.ENDPOINT_TWO, files={"file": file.getvalue()})
    if response.status_code == 200:
        return io.BytesIO(response.content)
    else:
        raise Exception(f"Unexpected status code: {response.status_code}, Response: {response.text}")
