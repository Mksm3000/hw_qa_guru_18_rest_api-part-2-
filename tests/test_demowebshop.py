import time

from pages.product_page import laptop, smartphone
from pages.cart_page import cart
import pytest


def test_adding_product_in_cart():
    cart.add_product_to_cart(laptop)
    cart.add_product_to_cart(smartphone)


def test_removing_product_from_cart():
    cart.remove_product_from_cart(smartphone)


