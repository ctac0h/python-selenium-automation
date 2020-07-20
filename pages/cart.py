from pages.base_page import Page
from selenium.webdriver.common.by import By


class Cart(Page):
    EMPTY_CART = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty')

    def verify_empty_cart(self, expected_text):
        actual_text = self.wait_for_element(self.EMPTY_CART).text
        assert actual_text == expected_text, 'Cart is not empty'
