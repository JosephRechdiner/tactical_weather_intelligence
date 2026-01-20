import mysql
from mysql.connector import MySQLConnection 
from datetime import datetime

class RecordsService:
    @staticmethod
    def insert_records(records: list[dict], cnx: MySQLConnection):
        query = 'INSERT INTO records_weather (timestamp, location_name, country, latitude, longitude, temperature, wind_speed, humidity, temperature_category, wind_category)' \
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            cursor = cnx.cursor(dictionary=True)
            for record in records:
                record["timestamp"] = datetime.strptime(record["timestamp"], '%Y-%m-%d %H:%M:%S')
                cursor.execute(query, (record["timestamp"], record["location_name"], record["country"], record["latitude"], record["longitude"],
                                       record["temperature"], record["wind_speed"], record["humidity"], record["temperature_category"], record["wind_category"],))
            cnx.commit()
            return {"msg": "records inserted succesfully!"}
        except mysql.connector.Error as e:
            raise e

    @staticmethod
    def get_records(cnx: MySQLConnection):
        query = 'SELECT * FROM records_weat;'
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query) 
            return cursor.fetchall()
        except mysql.connector.Error as e:
            raise e
    
    @staticmethod
    def get_number_of_records_by_location(cnx: MySQLConnection):
        query = f'SELECT location_name, COUNT(*) AS count FROM records_weather GROUP BY location_name;'
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            raise e
        
    @staticmethod
    def get_avg_temp_by_location(cnx: MySQLConnection):
        query = f'SELECT location_name, AVG(temperature) AS average FROM records_weather GROUP BY location_name;'
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            raise e
        
    @staticmethod
    def get_max_wind_by_location(cnx: MySQLConnection):
        query = f'SELECT location_name, MAX(wind_speed) AS max_wind FROM records_weather GROUP BY location_name;'
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            raise e

    @staticmethod
    def get_location_by_extreme(cnx: MySQLConnection):
        query = f'SELECT location_name FROM records_weather WHERE (temperature_category = "hot" AND wind_category = "calm") OR (temperature_category = "cold" AND wind_category = "windy");'
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            raise e

