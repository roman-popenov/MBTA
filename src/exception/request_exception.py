class RequestException(Exception):
    """Superclass for all Exceptions raised during request calls to MBTA API. """
    pass


class NotFoundException(RequestException):
    """ Raised when search returns 404 (Not Found). """

    def __init__(self, response, query_val):
        parameter = response['errors'][0]['source']['parameter']
        reason = response['errors'][0]['title']
        message = f'{parameter}: {query_val} {reason}'
        super().__init__(message)


class ForbiddenException(RequestException):
    """ Raised when request returns a 403 HTTP error code. """

    def __init__(self, url):
        super().__init__(f'GET {url} returned - 403: Forbidden')


class BadRequest(RequestException):
    """ Raised if MBTA interpreted given request was invalid in syntax or in parameters. """

    def __init__(self, url, params):
        super().__init__(f"GET with params '{params}' on '{url}' returned - 400: Bad Request")


class QuotaException(RequestException):
    """ Raised when application has made too many requests using a given api key. """

    def __init__(self):
        super().__init__('429: Too Many Requests')
