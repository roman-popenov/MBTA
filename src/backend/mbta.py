import logging

from src.backend.client.query_client import QueryClient
from src.backend.infrastructure.prediction import Prediction
from src.backend.infrastructure.route import Route
from src.backend.infrastructure.stop import Stop
from src.backend.util.configuration import Configuration
from src.backend.util.constants import RouteType, RouteKeys, ResponseKeys, PredictionKeys

DEFAULT_CONFIGURATION_PATH = 'config/app_config.yml'
_logger = logging.getLogger(__name__)


class MBTA(object):

    def __init__(self, app_config_file_path=DEFAULT_CONFIGURATION_PATH):
        self.app_config = Configuration(app_config_file_path)
        self.app_config.load_configuration()
        self.client = QueryClient(self.app_config.api_key, self.app_config.mbta_root_url)
        self.routes = {}
        self.stops = {}

    def get_client(self):
        return self.client

    def fetch_routes(self):
        self.populate_routes_data()

    def fetch_stops(self, route_name):
        route = self.routes[route_name]
        route_stops = route.get_stops()
        if route_stops:
            return route_stops
        else:
            self.populate_stops_data(route)
            return route.get_stops()

    def populate_routes_data(self):
        route_response = self.client.mbta_request(
            Route.all_resources_path,
            **{RouteKeys.Type.value: f'{RouteType.LightRail.value},{RouteType.HeavyRail.value}'})

        if type(route_response) is list:
            for route_entry in route_response:
                results = MBTA.append_process_routes_response_object_data(route_entry)
                self.routes.update(results)
        else:
            MBTA.append_process_routes_response_object_data(route_response)

    def populate_stops_data(self, route):
        stop_response = self.client.mbta_request(Stop.all_resources_path, **{Route.resource_name: route.id})

        if type(stop_response) is list:
            for stop_entry in stop_response:
                self.append_stop_response_object_data(stop_entry, route, self.stops)
        else:
            self.append_stop_response_object_data(stop_response, route, self.stops)

    def get_predictions(self, route_name, stop_name, direction_id):
        prediction_times = []
        if stop_name not in self.stops:
            self.populate_stops_data(self.routes[route_name])

        if stop_name in self.stops:
            stop = self.stops[stop_name]
            prediction_response = self.client.mbta_request(Prediction.all_resources_path,
                                                           **{Stop.resource_name: stop.id,
                                                              PredictionKeys.DirectionId.value: direction_id})
            if type(prediction_response) is list:
                for prediction_entry in prediction_response:
                    MBTA.append_prediction_response_object_data(prediction_entry, prediction_times)
            else:
                MBTA.append_prediction_response_object_data(prediction_response, prediction_times)

        return prediction_times

    @staticmethod
    def append_prediction_response_object_data(prediction_response, prediction_times):
        prediction = Prediction(prediction_response[ResponseKeys.Id.value],
                                prediction_response[ResponseKeys.Attributes.value],
                                prediction_response[ResponseKeys.Relationships.value])
        prediction_time = prediction.arrival_time
        if prediction_time:
            prediction_times.append(prediction_time)

    @staticmethod
    def append_stop_response_object_data(stop_response, route, stops):
        stop = Stop(stop_response[ResponseKeys.Id.value], stop_response[ResponseKeys.Attributes.value],
                    stop_response[ResponseKeys.Relationships.value])
        stop_name = stop.name
        stops[stop_name] = stop
        route.add_stop(stop_name)

    @staticmethod
    def append_process_routes_response_object_data(route_response):
        routes = {}

        route = Route(route_response[ResponseKeys.Id.value], route_response[ResponseKeys.Attributes.value],
                      route_response[ResponseKeys.Relationships.value])
        routes[route.name] = route

        return routes
