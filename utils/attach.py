import json

import allure
from allure_commons.types import AttachmentType
from requests import Response


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png,
                  name='screenshot',
                  attachment_type=AttachmentType.PNG,
                  extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def request_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    allure.attach(body=response.request.method,
                  name="Method",
                  attachment_type=AttachmentType.TEXT)
    allure.attach(body=json.dumps(dict(response.request.headers), indent=4),
                  name="Request headers",
                  attachment_type=AttachmentType.JSON)

    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )


def response_attaching(response: Response):
    allure.attach(body=str(response.status_code),
                  name="Code",
                  attachment_type=AttachmentType.TEXT)
    allure.attach(body=json.dumps(dict(response.request.headers), indent=4),
                  name="Response headers",
                  attachment_type=AttachmentType.JSON)
    allure.attach(body=json.dumps(dict(response.cookies), indent=4),
                  name="Cookies",
                  attachment_type=AttachmentType.JSON)

    if response.text:
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
