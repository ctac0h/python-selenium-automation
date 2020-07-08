from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

text_to_search = "cancel order"
expected_text = "Cancel Items or Orders"

driver.get("https://www.amazon.com/gp/help/customer/display.html")

search_box = driver.find_element(By.CSS_SELECTOR, '#helpsearch')
search_box.send_keys(text_to_search)


go_button = driver.find_element(By.XPATH, "//*[@id='helpSearchSubmit']//input")
go_button.click()

first_result = driver.find_element(By.XPATH, "//div[@class='cs-help-search-results']//a[@class='a-link-normal']")
actual_text = first_result.text

assert actual_text == expected_text, f"Expected text is {expected_text}, but got {actual_text}"

driver.quit()

