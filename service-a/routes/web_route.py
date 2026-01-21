from datetime import datetime
from fastapi import APIRouter
from utils import ingest_weather_for_location
from services.web_service import send_to_service_b
from fastapi import HTTPException
from pydantic import BaseModel

class Records(BaseModel):
    data: list[dict]
    
web_router = APIRouter()

@web_router.post("/ingest")
def start_ingestion(location_name: str):
    try:
        data = ingest_weather_for_location(location_name)
        # data_obj = Records(data=data)
        return send_to_service_b(data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

