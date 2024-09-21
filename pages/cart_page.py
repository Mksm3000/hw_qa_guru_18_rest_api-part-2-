import allure
from selene import browser, by, have

from pages.product_page import ProductPage
from request import api_request


class CartPage:

    def add_product_to_cart(self, new_product: ProductPage):
        with allure.step('Login with API'):
            url = 'https://demowebshop.tricentis.com'
            endpoint = f'/addproducttocart/details/{new_product.id}/1'
            data = {f'addtocart_{new_product.id}.EnteredQuantity': new_product.count}
            response = api_request(url, endpoint=endpoint, method='POST', data=data)

            cookie = response.cookies.get('Nop.customer')

            browser.open('/cart')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
            browser.driver.refresh()

        with allure.step(f'Verify {new_product.name} in cart'):
            browser.element('.cart').element('.product').element(
                '.product-name').should(
                have.exact_text(new_product.name))

        with allure.step(f'Verify {new_product.count} for {new_product.name} in '
                         f'cart'):
            browser.element('.cart').element('.cart-item-row').element(
                '.qty-input').should(have.value(new_product.count))

    def remove_product_from_cart(self, new_product: ProductPage):
        with allure.step('Login with API'):
            url = 'https://demowebshop.tricentis.com'
            endpoint = f'/addproducttocart/details/{new_product.id}/1'
            data = {f'addtocart_{new_product.id}.EnteredQuantity': new_product.count}
            response = api_request(url, endpoint=endpoint, method='POST', data=data)

            cookie = response.cookies.get('Nop.customer')

            browser.open('/cart')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
            browser.driver.refresh()

        with allure.step(f'Remove {new_product.name} from cart'):
            new_product_row = browser.element('.cart-item-row').should(
                have.text(new_product.name))
            new_product_row.element('.remove-from-cart').element(
                by.name('removefromcart')).click()
            browser.should(have.no.text(new_product.name))


cart = CartPage()
