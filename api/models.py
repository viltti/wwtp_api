#from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
import os

class Data:
    @staticmethod
    def get_db_connection():
        DB_URL = os.getenv('DB_URL')
        engine = create_engine(DB_URL, poolclass=QueuePool, pool_recycle=600)
        return engine

    @staticmethod
    def get_data():
        timestamp = pd.Timestamp.now().floor('10min')
        query = f"SELECT * FROM wwtp_data WHERE index = '{timestamp}'"
        data = pd.read_sql_query(query, Data.get_db_connection())
        return data

    @staticmethod
    def get_history():
        timestamp = pd.Timestamp.now().floor('10min')
        query = f"SELECT * FROM wwtp_data WHERE index <= '{timestamp}'"
        data = pd.read_sql_query(query, Data.get_db_connection())
        return data

    @staticmethod
    def get_previous_day():
        timestamp = pd.Timestamp.now().floor('10min') - pd.DateOffset(days=1)
        query = f"SELECT * FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(days=1)}'"
        data = pd.read_sql_query(query, Data.get_db_connection())
        return data

    @staticmethod
    def get_previous_hour():
        timestamp = pd.Timestamp.now().floor('10min') - pd.DateOffset(hours=1)
        query = f"SELECT * FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(hours=1)}'"
        data = pd.read_sql_query(query, Data.get_db_connection())
        return data