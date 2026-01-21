from fastapi import APIRouter, Depends, HTTPException
from mysql.connector import MySQLConnection 
from db.connector import MySQLManager
from services.records_service import RecordsService
from models.schemas import Info

manager = MySQLManager()
records_router = APIRouter()

def create_db(cnx: MySQLConnection):
    query = 'CREATE DATABASE IF NOT EXISTS weather_db;'
    try:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
def use_db(cnx: MySQLConnection):
    query = 'USE weather_db;'
    try:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
def create_table(cnx: MySQLConnection):
    query = """
            CREATE TABLE IF NOT EXISTS records_weather (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME,
            location_name VARCHAR(255),
            country VARCHAR(255),
            latitude FLOAT,
            longitude FLOAT,
            temperature FLOAT,
            wind_speed FLOAT,
            humidity INT,
            temperature_category VARCHAR(255),
            wind_category VARCHAR(255)
        );
            """
    try:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
def init_db(cnx):
    try:
        create_db(cnx)
        use_db(cnx)
        create_table(cnx)
        cnx.commit()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@records_router.post("/records")
def post_records(records: Info, cnx: MySQLConnection = Depends(manager.get_cnx)):
    try:      
        return RecordsService.insert_records(records.data, cnx)
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