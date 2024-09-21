import allure
import requests
from selene import browser, by, have

from pages.product_page import ProductPage


class CartPage:

    def add_product_to_cart(self, new_product: ProductPage):
        with allure.step('Login with API'):
            url = f'https://demowebshop.tricentis.com/addproducttocart/details/{new_product.id}/1'
            payload = {f'addtocart_{new_product.id}.EnteredQuantity': new_product.count}
            result = requests.post(url, json=payload)

        with allure.step('Get cookie from API'):
            cookie = result.cookies.get('Nop.customer')

        with allure.step('Set cookie from API'):
            url = 'https://demowebshop.tricentis.com/cart'
            browser.open(url)
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
            browser.open(url)

    def verify_product_in_cart(self, new_product: ProductPage):
        with allure.step(f'Verify {new_product.name} in cart'):
            browser.element(by.xpath(
                f"//a[@class='product-name' and contains(text(), '{new_product.name}')]"))
        with allure.step(f'Verify {new_product.count} in cart'):
            browser.element(by.xpath(
                f"//a[@class='qty nobr' and contains(text(), '{new_product.count}')]"))

    # def remove_product_from_cart(self, new_product: ProductPage):
    #     with allure.step(f'Remove {new_product.name} from cart'):
    #         new_product_row = browser.element('.cart-item-row').element(
    #             '.product').should(have.text(new_product.name))
    #         remove_button = new_product_row.element('.remove-from-cart').element(
    #             by.name('removefromcart'))
    #         assert remove_button
    #         remove_button.click()
    #         browser.driver.refresh()
    #         browser.should(have.no.text(new_product.name))


cart = CartPage()
