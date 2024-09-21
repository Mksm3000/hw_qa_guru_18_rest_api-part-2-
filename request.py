import requests

from utils.attach import request_attaching, response_attaching
from utils.logging import request_logging, response_logging


def api_request(base_api_url, endpoint, method,
                data=None, params=None, allow_redirects=False):
    url = f"{base_api_url}{endpoint}"

    response = requests.request(method, url, data=data, params=params,
                                allow_redirects=allow_redirects)
    request_logging(response)
    request_attaching(response)

    response_logging(response)
    response_attaching(response)

    return response
