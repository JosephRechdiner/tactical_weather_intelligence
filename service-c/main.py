from fastapi import FastAPI
from routes.records_route import records_router

app = FastAPI()
app.include_router(records_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)