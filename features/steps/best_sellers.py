from selenium.webdriver.common.by import By
from behave import given, when, then
from features.steps.wrapper import *
from time import sleep


MENU_ITEMS = (By.XPATH, '//div[@id="zg_header"]//li')
HEADER = (By.CSS_SELECTOR,'#zg_banner_text_wrapper')


@given('Open Amazon Best Sellers page with {link}')
def open_best_sellers(context, link):
    context.driver.get(link)


@then('Verify Best Sellers menu has {number} links')
def verify_best_sellers_menu(context, number):
    context.menu_items = wait_for_elements(MENU_ITEMS)
    context.item_count = len(context.menu_items)
    assert context.item_count == int(number), f'Expected {number} Best Sellers menu links, but got {context.item_count}'


@then('Click on each menu item and verify correct page is opened')
def click_all_menu_items_and_verify_pages(context):
    for i in range(context.item_count):
        item_link = wait_for_elements(MENU_ITEMS)[i].find_element(By.CSS_SELECTOR, 'a')
        item_link_text = item_link.text.lower()
        item_link.click()
        sleep(1)
        header = wait_for_element(HEADER)
        assert item_link_text in header.text.lower(), 'Wrong header'
        assert wait_for_elements(MENU_ITEMS)[i].get_attribute("class").lower() == 'zg_selected', 'Selected menu item' \
                                                                                                 'was not highlighted'


