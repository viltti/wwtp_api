
from .resources import DataResource, DataHistoryResource, DataDayResource, DataHourResource

def initialize_routes(api):
    api.add_resource(DataResource, '/data')
    api.add_resource(DataHistoryResource, '/data/history')
    api.add_resource(DataDayResource, '/data/day')
    api.add_resource(DataHourResource, '/data/hour')
