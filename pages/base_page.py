from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def wait_for_element(self, locator):
        return self.driver.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_elements(self, locator):
        return self.driver.wait.until(EC.visibility_of_any_elements_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        return self.driver.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_disappear(self, locator):
        return self.driver.wait.until(EC.invisibility_of_element(locator))