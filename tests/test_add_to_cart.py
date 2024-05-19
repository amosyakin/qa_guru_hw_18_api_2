import allure
import pytest
from selene import browser

from qa_guru_hw_18_api_2.api import add_to_cart_response
from qa_guru_hw_18_api_2.model import cart_page


@allure.feature('Add to cart')
class TestAddToCart:

    url_add_to_cart = '/addproducttocart/catalog'

    @pytest.mark.parametrize('product_name, product_info', [
        ('Computing and Internet', '/13/1/1'),
        ('Blue Jeans', '/36/1/1'),
        ('Smartphone', '/43/1/1')])
    @allure.title('Add to cart {product_name}')
    def test_add_to_cart(self, base_url, product_name, product_info):
        url = base_url + self.url_add_to_cart + product_info

        with allure.step(f'Add product {product_name} to cart with API'):
            response = add_to_cart_response(url)

        with allure.step('Open cart'):
            with allure.step('Get cookie from API'):
                cookie = response.cookies.get('Nop.customer')

            with allure.step('Set cookie from API'):
                browser.open('/')
                browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
                browser.open('/cart')

        with allure.step('Verify successful add to cart'):
            cart_page.should_cart_have_product_name(product_name)
