from selenium.webdriver.common.by import By
from behave import given, when, then


CART_PAGE_URL = 'https://www.amazon.com/gp/cart/view.html'

ADD_TO_CART = (By.ID, "add-to-cart-button")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'span.sc-product-title')


@given('Open Amazon cart page')
def open_cart(context):
    context.driver.get(CART_PAGE_URL)


@when('CLick on Add to cart')
def click_on_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()


@then('Verify Cart is empty and {expected_text} displayed')
def verify_empty_cart(context, expected_text):
    context.app.cart.verify_empty_cart(expected_text)


@then('Verify presence of {product_title} in the cart')
def verify_presence_of_product(context, product_title):
    actual_title = context.driver.find_element(*PRODUCT_TITLE).text
    assert product_title in actual_title, f'{product_title} not found'


