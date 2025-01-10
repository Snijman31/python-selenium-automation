from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.CSS_SELECTOR, '[data-test="resultsHeading"]')

    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS)

    def verify_search_url(self, product):
        self.verify_partial_url(product)

    def add_to_cart(self, product):
        self.add_to_cart(product)

