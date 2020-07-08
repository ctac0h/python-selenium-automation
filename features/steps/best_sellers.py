from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


MENU_ITEMS = (By.XPATH, '//div[@id="zg_header"]//li')


@given('Open Amazon Best Sellers page with {link}')
def open_best_sellers(context, link):
    context.driver.get(link)


@then('Verify Best Sellers menu has {number} links')
def verify_best_sellers_menu(context, number):
    menu_items = context.driver.find_elements(*MENU_ITEMS)
    item_count = len(menu_items)
    assert item_count == int(number), f'Expected {number} Best Sellers menu links, but got {item_count}'
