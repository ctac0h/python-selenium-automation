from selenium.webdriver.common.by import By
from behave import given, then, when
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


WEBSITE_LINK = (By.XPATH, "//p[contains(text(),'Business website')]/..//a")
PAGE_TITLE = 'Jamba Juice'
original_window = []


@given('Open Yelp page')
def open_yelp(context):
    context.driver.get('https://www.yelp.com/biz/jamba-juice-san-jose-6?hrid=nBSa7yMmJub3z0wI4FFJIA')


@when('Click on a website link')
def click_link(context):
    original_window.append(context.driver.current_window_handle)
    context.driver.find_element(*WEBSITE_LINK).click()
    print(original_window)


@when('Switch to a new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    for window in context.driver.window_handles:
        if window not in original_window:
            context.driver.switch_to_window(window)


@then('The company\'s website is open')
def verify_website(context):
    assert PAGE_TITLE in context.driver.title, 'Wrong title'


@then('a user can close the new window and go to the original')
def close_window_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to_window(original_window[0])








