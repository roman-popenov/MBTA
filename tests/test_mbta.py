from unittest import TestCase

from src.backend.mbta import MBTA


class TestMBTA(TestCase):
    """ Tests for MBTA object. """

    def test_mbta_creation(self):
        mbta = MBTA('data/test_app_config.yml')
        self.assertEqual(mbta.stops, {})
        self.assertEqual(mbta.routes, {})

    # TODO [rpope]: extend test coverage
    def test_get_client(self):
        self.fail()

    def test_fetch_routes(self):
        self.fail()

    def test_fetch_stops(self):
        self.fail()

    def test_populate_routes_data(self):
        self.fail()

    def test_populate_stops_data(self):
        self.fail()

    def test_get_predictions(self):
        self.fail()

    def test_append_prediction_response_object_data(self):
        self.fail()

    def test_append_stop_response_object_data(self):
        self.fail()

    def test_append_process_routes_response_object_data(self):
        self.fail()
