from selenium.webdriver.common.by import By
from behave import given, then


SECTIONS = (By.CSS_SELECTOR, '.s-result-list.s-col-2.wfm-desktop-list-font-unset.s-height-equalized')
ITEM_DESCRIPTIONS = (By.CSS_SELECTOR, '.s-result-item div.a-text-left')
PRODUCT_NAME = (By.CSS_SELECTOR, '.wfm-sales-item-card__product-name')
REGULAR_PRICE = (By.CSS_SELECTOR, '.wfm-sales-item-card__regular-price')
fail_list = []


@given('Open Amazon Wholefoods deals page {link}')
def open_deals(context, link):
    context.driver.get(link)


@then('Verify all products have name and regular price')
def verify_name_and_regular(context):
    products = context.driver.find_elements(*SECTIONS)[-1].find_elements(*ITEM_DESCRIPTIONS)
    for product in products:
        name = product.find_element(*PRODUCT_NAME).text
        regular = product.find_element(*REGULAR_PRICE).text
        if name == '' or "regular" not in regular.lower():
            fail_list.append([name, regular])
    if fail_list:
        for i in fail_list:
            print(i)
    assert not fail_list




