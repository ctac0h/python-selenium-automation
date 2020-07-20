from pages.base_page import Page
from selenium.webdriver.common.by import By


class TopNavMenu(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.XPATH, "//*[@value='Go']")
    ORDERS_BUTTON = (By.ID, "nav-orders")
    CART_BUTTON = (By.ID, 'nav-cart')
    HAMBURGER_MENU = (By.ID, 'nav-hamburger-menu')

    def input_search_word(self, search_word):
        self.input(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)

    def click_orders_button(self):
        self.wait_for_element_to_be_clickable(self.ORDERS_BUTTON)
        self.click(*self.ORDERS_BUTTON)

    def click_cart_button(self):
        self.wait_for_element_to_be_clickable(self.CART_BUTTON).click()

    def open_h_menu(self):
        self.wait_for_element_to_be_clickable(self.HAMBURGER_MENU).click()
