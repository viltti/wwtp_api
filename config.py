import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']
    BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD')