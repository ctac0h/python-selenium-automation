from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("\"Sign in\" page opened")
def verify_sign_in_page(context, expected_title):
    page_title = context.driver.title
    assert page_title == expected_title, f"Expected title is: {expected_title}, but got {page_title}"
