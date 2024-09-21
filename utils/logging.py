import logging
from requests import Response


def request_logging(response: Response):
    logging.info("Request: " + response.request.url)
    logging.info("Request method: " + response.request.method)
    logging.info("Request headers: " + str(response.request.headers))
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)


def response_logging(response: Response):
    logging.info("Response code: " + str(response.status_code))
    logging.info("Response headers: " + str(response.headers))
    if response.text:
        logging.info("INFO Response body: " + response.text)

