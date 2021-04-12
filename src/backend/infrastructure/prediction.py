from iso8601 import ParseError, parse_date

from src.backend.util.constants import PredictionKeys


class Prediction(object):
    """ This class represents a prediction. """

    all_resources_path = 'predictions'
    resource_name = 'prediction'

    def __init__(self, id, attributes, relationships):
        self.id = id
        self.attributes = attributes
        self.relationships = relationships

    @property
    def arrival_time(self):
        """
            When the current vehicle is expected to arrive. Returns None if this is the first stop.

            :return str:
                    The time the next train is arriving at station, parsed from an ISO8601 string.
        """
        try:
            iso_time = parse_date(self.attributes[PredictionKeys.ArrivalTime.value])
            return str(iso_time.time())
        except ParseError:
            return None

    @property
    def schedule_relationship(self):
        """
            A string describing how the predicted stop relates to a schedule.

            :return str:
                    The schedule relationship.
        """
        return self.attributes[PredictionKeys.ScheduleRelationShips.value]
