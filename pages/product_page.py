from pages.base_page import Page
from selenium.webdriver.common.by import By


class Product(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SIZE_SELECTION_TOOLTIP = (By.ID, 'a-popover-content-1')
    TOP_MENU = '//div[@id = "nav-subnav"]//a'
    TOP_MENU_TOOLTIP = (By.CSS_SELECTOR, '.mega-menu')

    def open_product(self, pid):
        self.open_page(f'dp/{pid}')

    def hover_add_to_cart(self):
        cart_button = self.driver.find_element(*self.ADD_TO_CART_BTN)
        self.actions.move_to_element(cart_button).perform()

    def verify_size_tooltip(self):
        self.wait_for_element(self.SIZE_SELECTION_TOOLTIP)

    def hover_over_product_top_menu(self, nth):
        product_top_menu_item = (By.XPATH, self.TOP_MENU+f'[{nth}]')
        menu_item = self.find_element(*product_top_menu_item)
        self.actions.move_to_element(menu_item).perform()

    def verify_product_top_menu_tooltip(self):
        self.wait_for_element_present(self.TOP_MENU_TOOLTIP)
