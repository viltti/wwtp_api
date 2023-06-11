from flask_restful import Resource
from flask import jsonify
from api.models import Data
from .auth import auth

class DataResource(Resource):
    @auth.login_required
    def get(self):
        data = Data.get_data()
        data_dict = data.to_dict(orient='records')
        return jsonify(data_dict)

class DataHistoryResource(Resource):
    @auth.login_required
    def get(self):
        data = Data.get_history()
        data_dict = data.to_dict(orient='records')
        return jsonify(data_dict)

class DataDayResource(Resource):
    @auth.login_required
    def get(self):
        data = Data.get_previous_day()
        data_dict = data.to_dict(orient='records')
        return jsonify(data_dict)

class DataHourResource(Resource):
    @auth.login_required
    def get(self):
        data = Data.get_previous_hour()
        data_dict = data.to_dict(orient='records')
        return jsonify(data_dict)