from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    RESULTS_INFO_TEXT = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")

    def verify_found_results_text(self, search_word):
        results_msg = self.find_element(*self.RESULTS_INFO_TEXT).text
        assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word,
                                                                                                results_msg)