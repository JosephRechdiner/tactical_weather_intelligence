from pydantic import BaseModel, Field
from datetime import datetime



class Weather_information(BaseModel):
    timestamp: datetime
    country: str
    latitude: float = Field(...,ge=-90,le=90)
    longitude: float = Field(...,gt=0, le=180)
    temperature: float
    temperature_unit: str
    wind_speed: float
    wind_speed_unit: str
    humidity: int
    humidity_unit: str

