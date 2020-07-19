from selenium.webdriver.common.by import By
from behave import given, then, when
from features.steps.wrapper import *
from time import sleep


WEBSITE_LINK = (By.XPATH, "//p[contains(text(),'Business website')]/..//a")
PAGE_TITLE = 'Jamba Juice'
JAMBA_LOGO = (By.CSS_SELECTOR, '.site-logo-component')


@given('Open Yelp page')
def open_yelp(context):
    context.driver.get('https://www.yelp.com/biz/jamba-juice-san-jose-6?hrid=nBSa7yMmJub3z0wI4FFJIA')


@when('Click on a website link')
def click_link(context):
    context.driver.find_element(*WEBSITE_LINK).click()


@then('The company\'s website is open')
def verify_website(context):
    wait_for_element(JAMBA_LOGO)
    assert PAGE_TITLE in context.driver.title, 'Wrong title'









