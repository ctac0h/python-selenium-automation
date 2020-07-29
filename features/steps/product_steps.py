from behave import then, when


@when('Hover over Add To Cart button')
def hover_over_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()


@then('Verify size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.hover_add_to_cart()


@when('Hover over {nth} product top menu item')
def hover_over_product_top_menu(context,nth):
    context.app.product_page.hover_over_product_top_menu(nth)


@then('Product top menu tooltip is shown')
def verify_product_top_menu_tooltip(context):
    context.app.product_page.verify_product_top_menu_tooltip()

