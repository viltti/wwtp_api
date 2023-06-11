#from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.pool import QueuePool
import os

class Data:
    @staticmethod
    def get_db_connection():
        DB_URL = os.getenv('DB_URL')
        engine = create_engine(DB_URL, poolclass=QueuePool, pool_recycle=600)
        return engine

    @staticmethod
    def get_data(variable = None):
        timestamp = pd.Timestamp.now().floor('10min')
        if variable is not None:
            query = f"SELECT index, {variable} FROM wwtp_data WHERE index = '{timestamp}'"
        else:
            query = f"SELECT * FROM wwtp_data WHERE index = '{timestamp}'"
        data = pd.read_sql_query(query, Data.get_db_connection())
        return data

    @staticmethod
    def get_history(variable = None):
        timestamp = pd.Timestamp.now().floor('10min')
        if variable is not None:
            query = f"SELECT index, {variable} FROM wwtp_data WHERE index <= '{timestamp}'"
        else:
            query = f"SELECT * FROM wwtp_data WHERE index <= '{timestamp}'"
        data = pd.read_sql_query(query, Data.get_db_connection())
        return data

    @staticmethod
    def get_previous_day(variable = None):
        timestamp = pd.Timestamp.now().floor('10min') - pd.DateOffset(days=1)
        if variable is not None:
            query = f"SELECT index, {variable} FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(days=1)}'"
        else:
            query = f"SELECT * FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(days=1)}'"
        data = pd.read_sql_query(query, Data.get_db_connection())
        return data

    @staticmethod
    def get_previous_hour(variable = None):
        timestamp = pd.Timestamp.now().floor('10min') - pd.DateOffset(hours=1)
        if variable is not None:
            query = f"SELECT index, {variable} FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(hours=1)}'"
        else:
            query = f"SELECT * FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(hours=1)}'"
        data = pd.read_sql_query(query, Data.get_db_connection())
        return data
    
    @staticmethod
    def get_variables():
        engine = Data.get_db_connection()
        metadata = MetaData()
        wwtp_data = Table('wwtp_data', metadata, autoload_with=engine)
        variables = [column.key for column in wwtp_data.columns if column.key != 'index']
        return variables