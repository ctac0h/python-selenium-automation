from behave import given, when, then
from time import sleep


@when("Click on Orders button")
def click_orders_button(context):
    context.app.top_nav_menu.click_orders_button()


@when('Search for {search_word}')
def input_search(context, search_word):
    context.app.top_nav_menu.input_search_word(search_word)


@when('Click on Cart icon')
def click_on_cart(context):
    context.app.top_nav_menu.click_cart_button()


@when('Open hamburger menu')
def open_h_menu(context):
    context.app.top_nav_menu.open_h_menu()
    sleep(1)


@when('Select {alias} department')
def select_department(context, alias):
    context.app.top_nav_menu.select_department(alias)


@then('{selected_dep} department is selected')
def verify_selected_department(context, selected_dep):
    context.app.top_nav_menu.verify_selected_department(selected_dep)