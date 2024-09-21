from pages.product_page import laptop, smartphone
from pages.cart_page import cart
import pytest


@pytest.mark.parametrize('product', [laptop, smartphone], ids=['laptop','smartphone'])
def test_adding_verifying_removing_in_cart(product):
    cart.add_product_to_cart(product)
    cart.verify_product_in_cart(product)
    cart.remove_product_from_cart(product)


