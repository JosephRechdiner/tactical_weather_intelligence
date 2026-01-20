from fastapi import FastAPI, HTTPException, APIRouter

app = FastAPI()
router = APIRouter()

@router.post('/ingest')
def post_ingest():
    pass
