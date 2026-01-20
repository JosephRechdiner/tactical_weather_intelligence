from fastapi import FastAPI, HTTPException, APIRouter
import models
import utils

app = FastAPI()
router = APIRouter()

@router.post('/ingest')
def post_ingest(info: models.Weather_information):
    try:
        utils.Data_hendler(info)
        return {'massege': 'good'}
    except HTTPException as e:
        return {'massege': str(e)}

