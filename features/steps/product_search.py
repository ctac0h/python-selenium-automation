from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.XPATH, "//*[@value='Go']")
RESULTS_INFO_TEXT = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
FIRST_RESULT = (By.XPATH, "//div[contains(@class,'s-main-slot')]/div[@data-index='2']")
SEARCH_RESULTS = (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')


@when('Click on first result')
def first_result_click(context):
    context.driver.find_element(*FIRST_RESULT).click()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.search_results.verify_found_results_text(search_word)


@then('Verify number of elements is equal to {number}')
def count_elements(context, number):
    search_results = context.driver.find_elements(*SEARCH_RESULTS)
    results_len = len(search_results)
    print(results_len)
    if results_len == 60:
        print('Everything is on the page')
    elif results_len > 0:
        print('Some elements are located')
    else:
        print("Nothing is found on the page")
