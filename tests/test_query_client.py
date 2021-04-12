import json
from unittest import TestCase
from unittest.mock import patch

from src.backend.client.query_client import QueryClient
from src.exception.request_exception import NotFoundException, ForbiddenException, QuotaException

TEST_CONFIG_FILE = 'data/test_app_config.yml'

DATA = {"data": {"attributes": {"color": "DA291C", "description": "Rapid Transit",
                                "direction_destinations": ["Mattapan", "Ashmont"],
                                "direction_names": ["Outbound", "Inbound"], "fare_class": "Rapid Transit",
                                "long_name": "Mattapan Trolley", "short_name": "", "sort_order": 10011,
                                "text_color": "FFFFFF", "type": 0}, "id": "Mattapan",
                 "relationships": {"line": {"data": {"id": "line-Mattapan"}}, "route_patterns": {}}},
        "jsonapi": {"version": "1.0"}}


class MockRequest:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mock_error(*args, **kwargs):
    return MockRequest(json.loads(
        '{"errors":[{"title": "NotFound", "status": "404", "source": {"parameter": "id"}, "code": "not_found"}]}'
    ),
        404
    )


class TestQueryClient(TestCase):
    """ Tests for Query client object. """

    def setUp(self):
        self.client = QueryClient('some_test_api')

    def test_set_user_agent(self):
        self.client.user_agent = 'Test-Agent'
        self.assertEqual(self.client.user_agent, 'Test-Agent')

    def test_apikey_exits(self):
        self.assertEqual(self.client.api_key, 'some_test_api')

    @patch('requests.get', side_effect=lambda *a, **kw: MockRequest(DATA, 200))
    def test_clean_request(self, mock):
        response = self.client.mbta_request('base_route')
        filtered_data = {key: DATA['data'][key] for key in {'id', 'attributes', 'relationships'}}
        self.assertEqual(response, filtered_data)

    @patch('requests.get', side_effect=mock_error)
    def test_handle_404(self, mock):
        with self.assertRaises(NotFoundException):
            self.client.mbta_request('bad_route')

    @patch('requests.get', side_effect=lambda *a, **kw: MockRequest(DATA, 403))
    def test_handle_403(self, mock):
        with self.assertRaises(ForbiddenException):
            self.client.mbta_request('bad_route')

    @patch('requests.get', side_effect=lambda *a, **kw: MockRequest(DATA, 429))
    def test_handle_quota_exceeded(self, mock):
        with self.assertRaises(QuotaException):
            self.client.mbta_request('too_many')
