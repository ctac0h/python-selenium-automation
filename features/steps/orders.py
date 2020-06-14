from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_BUTTON = (By.ID, "nav-orders")
EXPECTED_TITLE = "Amazon Sign-In"


@given("Open Amazon Page")
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when("Click on \"Orders\" button")
def click_orders_button(context):
    context.driver.find_element(*ORDERS_BUTTON).click()
    sleep(1)


@then("\"Sign in\" page opened")
def verify_sign_in_page(context):
    page_title = context.driver.title
    assert page_title == EXPECTED_TITLE, f"Expected title is: {EXPECTED_TITLE}, but got {page_title}"