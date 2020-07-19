from selenium.webdriver.support import expected_conditions as EC

driver = None


def wait_for_element(locator):
    return driver.wait.until(EC.visibility_of_element_located(locator))


def wait_for_elements(locator):
    return driver.wait.until(EC.visibility_of_any_elements_located(locator))


def wait_for_element_to_be_clickable(locator):
    return driver.wait.until(EC.element_to_be_clickable(locator))


def wait_for_element_to_disappear(locator):
    return driver.wait.until(EC.invisibility_of_element(locator))
