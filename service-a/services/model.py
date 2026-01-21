from pydantic import BaseModel    

class Weather_information_list(BaseModel):
    data: list[dict]