from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BOX = (By.CSS_SELECTOR, '#helpsearch')
GO_BUTTON = (By.XPATH, "//*[@id='helpSearchSubmit']//input")
FIRST_RESULT = (By.XPATH, "//div[@class='cs-help-search-results']//a[@class='a-link-normal']")
AMAZON_HELP_PAGE = "https://www.amazon.com/gp/help/customer/display.html"


@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get(AMAZON_HELP_PAGE)


@when('Input {search_word} to help search')
def input_search(context, search_word):
    search_box = context.driver.find_element(*SEARCH_BOX)
    search_box.clear()
    search_box.send_keys(search_word)
    sleep(2)


@when('Click help search button')
def click_go(context):
    context.driver.find_element(*GO_BUTTON).click()


@then('Help search results for {search_word} shown')
def verify_results(context,search_word):
    first_result = context.driver.find_element(*FIRST_RESULT)
    actual_text = first_result.text
    assert actual_text == search_word, f"Expected text is {search_word}, but got {actual_text}"
