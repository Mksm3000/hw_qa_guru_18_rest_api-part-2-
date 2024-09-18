import os
from os.path import join, dirname
from typing import Dict, Any

import allure
import pytest
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selene import browser
from selene.support.conditions import have

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')

WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_login_via_api():
    with step("Login with API"):
        result = requests.post(
            url=API_URL + "/login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )
        allure.attach(body=result.text, name="Response",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies",
                      attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Get cookie from API"):
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")

    with step("Set cookie from API"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))


@pytest.mark.parametrize('item', [
    pytest.param({'14.1-inch Laptop': {'item_id': 31, 'item_count': 2}},
                 id='14.1-inch Laptop'),
    pytest.param({'Smartphone': {'item_id': 43, 'item_count': 3}}, id='Smartphone')])
def test_adding_item_to_cart_via_api(item: Dict[str, Any]):
    name = list(item.keys())[0]
    with step(f"Add {name} to cart with API"):
        item_id = item[name]['item_id']
        item_count = item[name]['item_count']
        result = requests.post(
            url=API_URL + f"addproducttocart/details/{item_id}/1",
            data={f'addtocart_{item_id}.EnteredQuantity': item_count},
            allow_redirects=False
        )
