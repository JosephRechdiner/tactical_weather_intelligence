from fastapi import FastAPI
from routes.records_route import records_router


app = FastAPI()
app.include_router(records_router)
