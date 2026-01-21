import os
import requests
from pydantic import BaseModel

class Item(BaseModel):
    data: list[dict]

INTERNAL_URL = os.getenv("INTERNAL_URL")

def send_to_service_b(data):
    data = Item(data=data)
    try:
        response = requests.post(INTERNAL_URL, json=data.model_dump(mode='json'))
        return response.json()
    except Exception as e:
        raise e
