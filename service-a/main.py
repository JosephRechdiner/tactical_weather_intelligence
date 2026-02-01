from fastapi import FastAPI
from routes.web_route import web_router


app = FastAPI()

app.include_router(web_router)


