from selenium.webdriver.common.by import By
from behave import given, then, when
from selenium.webdriver.support import expected_conditions as EC


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





