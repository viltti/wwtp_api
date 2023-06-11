from flask import Blueprint
from flask_restful import Api
from .routes import initialize_routes

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

initialize_routes(api)