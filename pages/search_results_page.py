from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.CSS_SELECTOR, '[data-test="resultsHeading"]')

    def verify_search_results(self):
        sleep(5)
        actual_result = self.driver.find_element(*self.SEARCH_RESULTS).text
        assert 'juice' in actual_result, f'Expected text juice not in actual {actual_result})'



