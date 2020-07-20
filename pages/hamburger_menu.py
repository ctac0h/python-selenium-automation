from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Hamburger(Page):
    H_MENU = (By.CSS_SELECTOR, '.hmenu.hmenu-visible')
    H_ITEM = (By.CSS_SELECTOR, '.hmenu-item:not(.hmenu-title):not(.hmenu-back-button)')

    def get_items(self):
        menu = self.find_element(*self.H_MENU)
        menu_elements = menu.find_elements(*self.H_ITEM)
        return menu_elements

    def click_element_by_id(self, item_id: int):
        self.get_items()[item_id].click()
        sleep(1)

    def click_element_by_text(self, item_text: str):
        for element in self.get_items():
            if element.text.lower() == item_text.lower():
                element.click()
        sleep(1)

    def verify_number_of_items(self, number):
        actual_number = str(len(self.get_items()))
        assert actual_number == number, f'Expected {number} items, but got {actual_number}'


