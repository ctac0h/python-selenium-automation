from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_BUTTON = (By.ID, "nav-orders")
EXPECTED_TITLE = "Amazon Sign-In"


@when("Click on \"Orders\" button")
def click_orders_button(context):
    context.driver.find_element(*ORDERS_BUTTON).click()
    sleep(1)


@then("Verify {expected_page_title} page opened")
def verify_sign_in_page(context,expected_page_title):
    actual_page_title = context.driver.title
    assert actual_page_title == expected_page_title, f"Expected title is: {expected_page_title}, but got {actual_page_title}"
