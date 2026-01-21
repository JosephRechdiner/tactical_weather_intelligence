from fastapi import APIRouter, Depends, HTTPException
from mysql.connector import MySQLConnection 
from db.connector import MySQLManager
from services.records_service import RecordsService
from models.schemas import Info

manager = MySQLManager()
records_router = APIRouter()

@records_router.post("/records")
def post_records(records: Info, cnx: MySQLConnection = Depends(manager.get_cnx)):
    try:
        print(records.data)
        return {"msg": "ok"}
        # return RecordsService.insert_records(records.data, cnx)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@records_router.get("/all-records")
def get_all_records(cnx: MySQLConnection = Depends(manager.get_cnx)):
    try:
        return RecordsService.get_records(cnx)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@records_router.get("/records/count")
def get_records_by_location(cnx: MySQLConnection = Depends(manager.get_cnx)):
    try:
        return RecordsService.get_number_of_records_by_location(cnx)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@records_router.get("/records/avg-temperture")
def get_avg_temperture_by_location(cnx: MySQLConnection = Depends(manager.get_cnx)):
    try:
        return RecordsService.get_avg_temp_by_location(cnx)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@records_router.get("/records/max-wind")
def get_max_wind(cnx: MySQLConnection = Depends(manager.get_cnx)):
    try:
        return RecordsService.get_max_wind_by_location(cnx)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@records_router.get("/records/extreme")
def get_extreme(cnx: MySQLConnection = Depends(manager.get_cnx)):
    try:
        return RecordsService.get_location_by_extreme(cnx)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))