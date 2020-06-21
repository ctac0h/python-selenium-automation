from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_BUTTON = (By.ID, "nav-orders")



@given("Open Amazon Page")
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when("Click on \"Orders\" button")
def click_orders_button(context):
    context.driver.find_element(*ORDERS_BUTTON).click()
    sleep(1)

