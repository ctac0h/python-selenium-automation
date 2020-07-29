from selenium.webdriver.common.by import By
from behave import given, then
import json


EXPECTED_COLORS = ['emerald', 'ivory', 'navy', 'black']
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name span.selection')


@then('Verify user can select through {colors}')
def verify_color_selection(context, colors):
    expected_colors = json.loads(colors)
    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for i, color in enumerate(color_options):
        color.click()
        assert context.driver.find_element(*SELECTED_COLOR).text.lower() == expected_colors[i].lower()
