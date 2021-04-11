from src.backend.util.constants import RouteKeys, ResponseKeys


class Route(object):
    """ This class represents a route. """

    all_resources_path = 'routes'
    resource_name = 'route'

    def __init__(self, id, attributes, relationships):
        self.id = id
        self.attributes = attributes
        self.relationships = relationships
        self.stops = []

    def get_stops(self):
        return self.stops

    def add_stop(self, stop_name):
        self.stops.append(stop_name)

    @property
    def destinations(self):
        return self.attributes[RouteKeys.DirectionDestination.value][0], \
               self.attributes[RouteKeys.DirectionDestination.value][1]

    @property
    def directions(self):
        """
            Stop direction friendly names.

            :return str:
        """

        return self.attributes[RouteKeys.DirectionName.value][0], self.attributes[RouteKeys.DirectionName.value][1]

    @property
    def route_type(self):
        return self.attributes[RouteKeys.Type.value]

    @property
    def name(self):
        return self.attributes[RouteKeys.Name.value]

    @property
    def line(self):
        """ Returns the id of the line related to the route """
        return self.relationships[RouteKeys.Line.value][ResponseKeys.Data.value][ResponseKeys.Id.value]
