from fastapi import FastAPI
from routes.records_route import records_router
from contextlib import asynccontextmanager
from routes.records_route import init_db, manager




@asynccontextmanager
async def lifespan(app: FastAPI):
    cnx = manager.get_cnx()
    init_db(cnx)
    yield
    
app = FastAPI(lifespan=lifespan)
app = FastAPI()
app.include_router(records_router)

