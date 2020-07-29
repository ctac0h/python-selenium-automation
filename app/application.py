from pages.top_nav_menu import *
from pages.search_results import SearchResults
from pages.cart import Cart
from pages.hamburger_menu import Hamburger
from pages.product_page import Product


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        self.search_results = SearchResults(self.driver)
        self.cart = Cart(self.driver)
        self.hmenu = Hamburger(self.driver)
        self.product_page = Product(self.driver)
