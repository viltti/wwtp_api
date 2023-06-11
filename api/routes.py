
from .resources import (DataResource, DataHistoryResource, DataDayResource, 
                        DataHourResource, VariablesResource, DataVariableResource,
                        DataVariableHistoryResource, DataVariableDayResource, DataVariableHourResource)

def initialize_routes(api):

    # Routes /api/data/... fetch the data of all variables

    # get the current data
    api.add_resource(DataResource, '/data')
    # get all available history data
    api.add_resource(DataHistoryResource, '/data/history')
    # get the data of last day
    api.add_resource(DataDayResource, '/data/day')
     # get the data of last hour
    api.add_resource(DataHourResource, '/data/hour')

    # get feature names
    api.add_resource(VariablesResource, '/variables')
    
    # Routes /api/variable/... fetch the data of one variable

    # get the current data of one variable
    api.add_resource(DataVariableResource, '/data/variable/<string:variable>')
    # get all available history data of one variable
    api.add_resource(DataVariableHistoryResource, '/data/variable/<string:variable>/history')
    # get the data of one variable last day
    api.add_resource(DataVariableDayResource, '/data/variable/<string:variable>/day')
    # get the data of one variable last hour
    api.add_resource(DataVariableHourResource, '/data/variable/<string:variable>/hour')
