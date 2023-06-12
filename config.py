import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']
    BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD')

    ENGINE = create_engine(SQLALCHEMY_DATABASE_URI, poolclass=QueuePool, pool_recycle=600)
    SESSION = sessionmaker(bind=ENGINE)