from fastapi import FastAPI, HTTPException, APIRouter
import models
import utils



app = FastAPI()
router = APIRouter()
send_service = utils.Send_data()


@router.post('/ingest')
def post_ingest(info: list[models.Weather_information]):
    try:
        data = utils.Data_hendler(info)
        data = data.return_data_dict()
        send_service.send_data(data)
        return {'massege': 'data send'}
    except HTTPException as e:
        return {'massege': str(e)}


