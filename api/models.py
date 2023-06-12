import pandas as pd
from sqlalchemy import MetaData, Table
from flask import current_app
from contextlib import contextmanager

class Data:

    @staticmethod
    @contextmanager
    def get_db_session():
        Session = current_app.config['SESSION']
        session = Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def get_data(variable = None):
        timestamp = pd.Timestamp.now().floor('10min')
        if variable is not None:
            query = f"SELECT index, {variable} FROM wwtp_data WHERE index = '{timestamp}'"
        else:
            query = f"SELECT * FROM wwtp_data WHERE index = '{timestamp}'"
        with Data.get_db_session() as session:
            data = pd.read_sql_query(query, session.connection())
        return data

    @staticmethod
    def get_history(variable = None):
        timestamp = pd.Timestamp.now().floor('10min')
        if variable is not None:
            query = f"SELECT index, {variable} FROM wwtp_data WHERE index <= '{timestamp}'"
        else:
            query = f"SELECT * FROM wwtp_data WHERE index <= '{timestamp}'"
        with Data.get_db_session() as session:
            data = pd.read_sql_query(query, session.connection())
        return data

    @staticmethod
    def get_previous_day(variable = None):
        timestamp = pd.Timestamp.now().floor('10min') - pd.DateOffset(days=1)
        if variable is not None:
            query = f"SELECT index, {variable} FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(days=1)}'"
        else:
            query = f"SELECT * FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(days=1)}'"
        with Data.get_db_session() as session:
            data = pd.read_sql_query(query, session.connection())
        return data

    @staticmethod
    def get_previous_hour(variable = None):
        timestamp = pd.Timestamp.now().floor('10min') - pd.DateOffset(hours=1)
        if variable is not None:
            query = f"SELECT index, {variable} FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(hours=1)}'"
        else:
            query = f"SELECT * FROM wwtp_data WHERE index BETWEEN '{timestamp}' AND '{timestamp + pd.DateOffset(hours=1)}'"
        with Data.get_db_session() as session:
            data = pd.read_sql_query(query, session.connection())
        return data
    
    @staticmethod
    def get_variables():
        with Data.get_db_session() as session:
            metadata = MetaData()
            wwtp_data = Table('wwtp_data', metadata, autoload_with=session.connection())
            variables = [column.key for column in wwtp_data.columns if column.key != 'index']
        return variables