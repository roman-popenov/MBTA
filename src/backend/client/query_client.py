import requests

from src.backend.util.constants import ResponseKeys, ClientHeaderKeys
from src.exception.request_exception import RequestException, QuotaException, ForbiddenException, NotFoundException

DEFAULT_ROOT_URL = 'https://api-v3.mbta.com'
DEFAULT_USER_AGENT = 'NUMERATED.MBTA V1.0'


def apply_request_filters(**filters):
    """ Wraps filter parameter keys to be 'filter[key]': value so it can be passed as query parameters to request """

    keys = filters.keys()
    return {f'filter[{key}]': filters[key] for key in keys}


class QueryClient(object):
    """
        A wrapper class for API requests to MBTA.
        Requires credentials.

        Parameters
        ----------
        :param api_key: str
                Unique identifier used to authenticate a user, developer, or calling program to an API
        :param root_url: str, default 'DEFAULT_ROOT_URL'
                Starting point of the MBTA API
    """

    def __init__(self, api_key, root_url=DEFAULT_ROOT_URL):
        self.root_url = root_url
        self.api_key = api_key
        self.headers = {
            ClientHeaderKeys.Api.value: api_key,
            ClientHeaderKeys.UserAgent.value: DEFAULT_USER_AGENT
        }

    def mbta_request(self, resource, **params):
        url = f'{self.root_url}/{resource}'
        request = requests.get(
            url,
            headers=self.headers,
            params=apply_request_filters(**params)
        )

        if request.status_code == 200:
            return request.json()[ResponseKeys.Data.value]
        elif request.status_code == 403:
            raise ForbiddenException(url)
        elif request.status_code == 404:
            raise NotFoundException(request.json(), params)
        elif request.status_code == 429:
            raise QuotaException()
        else:
            raise RequestException(
                f'Error in getting response from {url}. '
                f'Returned {request.status_code} and {request.json()}'
            )
