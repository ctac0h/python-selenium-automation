from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HAMBURGER_MENU = (By.ID, 'sssnav-hamburger-menu')


@then('Locate a hamburger menu')
def locate_item(context):
    context.driver.find_element(*HAMBURGER_MENU)


