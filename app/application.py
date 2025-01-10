from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.side_nav_sign_in_page import SIDE_NAV_SIGN_IN
from pages.sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.cart_page =CartPage(driver)
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.side_nav_sign_in_page = SignInPage(driver)
        self.sign_in_page = SignInPage(driver)

