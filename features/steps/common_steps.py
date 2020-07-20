from selenium.webdriver.common.by import By
from behave import given, then, when
from selenium.webdriver.support import expected_conditions as EC


@given('Open Amazon page')
def open_amazon(context):
    context.app.page.open_page()


@then('Save current window handles')
def save_windows(context):
    context.original_windows = context.driver.window_handles
    context.current_window = context.driver.current_window_handle


@then('Switch to a new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    for window in context.driver.window_handles:
        if window not in context.original_windows:
            context.driver.switch_to_window(window)


@then('Close new window and switch back to original')
def close_window_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.current_window)


@then("Verify {expected_page_title} page opened")
def verify_page(context, expected_page_title):
    actual_page_title = context.driver.title
    assert actual_page_title == expected_page_title, f"Expected title is: {expected_page_title}, but got " \
                                                     f"{actual_page_title}"






