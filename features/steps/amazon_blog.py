from selenium.webdriver.common.by import By
from behave import when, then
from features.steps.wrapper import *


BLOG_MENU_BUTTON = (By.CSS_SELECTOR, 'button.ArticlePage-header-menuToggle')
MENU_ITEMS = (By.CSS_SELECTOR, '.Navigation-items-item')
CLOSE_BUTTON = (By.CSS_SELECTOR, '.ArticlePage-header-menuClose')


@when('Click on blog link “{link}”')
def click_blog_link(context, link):
    blog_link = (By.XPATH, f"//a[contains(text(),'{link}')]")
    wait_for_element_to_be_clickable(blog_link).click()


@then('Blog {link} is opened')
def verify_amazon_blog_opened(context, link):
    wait_for_element(BLOG_MENU_BUTTON)
    assert link in context.driver.current_url, 'Wrong page was opened'


@then('User can open and close Blog menu')
def verify_amazon_blog_menu(context):
    wait_for_element_to_be_clickable(BLOG_MENU_BUTTON).click()
    assert wait_for_elements(MENU_ITEMS), 'No menu items'
    wait_for_element_to_be_clickable(CLOSE_BUTTON).click()
    assert wait_for_element_to_disappear(MENU_ITEMS), 'Unable to close menu'



