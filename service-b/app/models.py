from pydantic import BaseModel, Field
from datetime import datetime



class Weather_information(BaseModel):
    timestamp: str
    location_name: str
    country: str
    latitude: float = Field(...,ge=-90,le=90)
    longitude: float = Field(...,gt=0, le=180)
    temperature: float
    wind_speed: float
    humidity: int
    
class Weather_information_list(BaseModel):
    info: list[dict]
