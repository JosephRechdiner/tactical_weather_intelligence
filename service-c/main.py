from fastapi import FastAPI
from routes.records_route import records_router
import uvicorn

app = FastAPI()
app.include_router(records_router)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)