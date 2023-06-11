from flask_restful import Resource
from flask import jsonify
from api.models import Data
from .auth import auth

# Resources for all variables

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

# Resource for variable names

class VariablesResource(Resource):
    @auth.login_required
    def get(self):
        variables = Data.get_variables()
        return jsonify(variables)

# Resources for a specific variable's data

class DataVariableResource(Resource):
    @auth.login_required
    def get(self, variable):
        data = Data.get_data(variable)
        data_dict = data.to_dict(orient='records')
        return jsonify(data_dict)

class DataVariableHistoryResource(Resource):
    @auth.login_required
    def get(self, variable):
        data = Data.get_history(variable)
        data_dict = data.to_dict(orient='records')
        return jsonify(data_dict)

class DataVariableDayResource(Resource):
    @auth.login_required
    def get(self, variable):
        data = Data.get_previous_day(variable)
        data_dict = data.to_dict(orient='records')
        return jsonify(data_dict)

class DataVariableHourResource(Resource):
    @auth.login_required
    def get(self, variable):
        data = Data.get_previous_hour(variable)
        data_dict = data.to_dict(orient='records')
        return jsonify(data_dict)