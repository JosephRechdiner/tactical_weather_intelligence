from fastapi import FastAPI, HTTPException, APIRouter
import models

app = FastAPI()
router = APIRouter()

@router.post('/ingest')
def post_ingest(info: models.Weather_information):
    pass
