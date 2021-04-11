from unittest import TestCase

from src.backend.infrastructure.route import Route

DATA = {"data": {"attributes": {"color": "DA291C", "description": "Rapid Transit",
                                "direction_destinations": ["Ashmont/Braintree", "Alewife"],
                                "direction_names": ["Dir1", "Dir2"], "fare_class": "Rapid Transit",
                                "long_name": "Test Line", "short_name": "", "sort_order": 10010, "text_color": "FFFFFF",
                                "type": 1}, "id": "Red", "links": {"self": "/routes/Red"},
                 "relationships": {"line": {"data": {"id": "line-Red", "type": "line"}}, "route_patterns": {}},
                 "type": "route"},
        "jsonapi": {"version": "1.0"}}

EXPECTED_STOPS = ["test_stop", "test_stop1", "test_stop2"]
EXPECTED_TEST_LINE_NAME = "Test Line"
EXPECTED_DIRECTIONS = ("Dir1", "Dir2")


class TestRoute(TestCase):
    """ Tests for Route object. """

    def test_route_creation(self):
        Route(DATA['data']['id'], DATA['data']['attributes'], DATA['data']['relationships'])

    def test_get_stops(self):
        route = Route(DATA['data']['id'], DATA['data']['attributes'], DATA['data']['relationships'])
        route.add_stop("test_stop")
        route.add_stop("test_stop1")
        route.add_stop("test_stop2")

        self.assertEqual(route.get_stops(), EXPECTED_STOPS)

    def test_line_name(self):
        route = Route(DATA['data']['id'], DATA['data']['attributes'], DATA['data']['relationships'])

        self.assertEqual(route.name, EXPECTED_TEST_LINE_NAME)

    def test_directions(self):
        route = Route(DATA['data']['id'], DATA['data']['attributes'], DATA['data']['relationships'])

        self.assertEqual(route.directions, EXPECTED_DIRECTIONS)
