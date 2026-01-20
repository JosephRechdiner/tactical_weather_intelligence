import mysql.connector
import os


class MySQLManager:
    def __init__(self):
        self.config = {
        'user': os.getenv("MYSQL_USER"),
        'password': os.getenv("MYSQL_PASSWORD"),
        'host': os.getenv("MYSQL_HOST"),
        'database': os.getenv("MYSQL_DATABASE")
        }

    def get_cnx(self):
        try:
            cnx = mysql.connector.connect(**self.config)
            cnx.ping(reconnect=True, attempts=3, delay=0)
            return cnx
        except mysql.connector.Error as e:
            raise e
            