from pydantic import BaseModel

class Info(BaseModel):
    data: list[dict]