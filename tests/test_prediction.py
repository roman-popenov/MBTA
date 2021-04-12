from unittest import TestCase

from src.backend.infrastructure.prediction import Prediction

DATA = {"data": {"attributes": {"arrival_time": "2021-04-11T20:58:35-04:00",
                                "departure_time": "2021-04-11T20:59:12-04:00", "direction_id": 0,
                                "schedule_relationship": None, "status": None, "stop_sequence": 10},
                 "id": "prediction-47433795-70057-10",
                 "relationships": {"route": {"data": {"id": "Blue", "type": "route"}},
                                   "stop": {"data": {"id": "70057", "type": "stop"}},
                                   "trip": {"data": {"id": "47433795", "type": "trip"}},
                                   "vehicle": {"data": {"id": "B-546A0ACD", "type": "vehicle"}}},
                 "type": "prediction"}, "jsonapi": {"version": "1.0"}}

EXPECTED_ARRIVAL_TIME = '20:58:35'


class TestPrediction(TestCase):
    """ Tests for Prediction object. """

    def test_prediction_creation(self):
        Prediction(DATA['data']['id'], DATA['data']['attributes'], DATA['data']['relationships'])

    def test_arrival_time(self):
        prediction = Prediction(DATA['data']['id'], DATA['data']['attributes'], DATA['data']['relationships'])
        self.assertEqual(prediction.arrival_time, EXPECTED_ARRIVAL_TIME)
