from behave import given, when, then


@when('Click on menu item with text {text}')
def click_on_item_by_text(context, text):
    context.app.hmenu.click_element_by_text(text)


@then('Verify {number} items are present')
def verify_number_of_items(context, number):
    context.app.hmenu.verify_number_of_items(number)


