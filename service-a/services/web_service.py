import os
import requests

INTERNAL_URL = os.getenv("INTERNAL_URL")

def send_to_service_b(data):
    try:
        # response = requests.post(INTERNAL_URL, json=data.model_dump(mode='json'))
        response = requests.post(INTERNAL_URL, json=data)
        return {"msg": response.json()}
    except Exception as e:
        raise e
