from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes.records_route import records_router
from db.connector import MySQLManager

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     MySQLManager.connect()
#     yield
#     MySQLManager.disconnect()

app = FastAPI()
app.include_router(records_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)