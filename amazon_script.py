from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

text_to_search = "dress"

search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_field.send_keys(text_to_search)
go_button = driver.find_element(By.XPATH, "//*[@value='Go']")
go_button.click()

actual_text = driver.find_element(By.XPATH, "//span[@data-component-type='s-result-info-bar']"
                                            "//span[contains(text(),'dress')]").text.strip('"')

print("Searched text:\t" + text_to_search + "\nActual text:\t" + actual_text)
assert text_to_search == actual_text

driver.quit()
