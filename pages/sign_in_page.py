from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class SignInPage(BasePage):
    SIGN_IN_PAGE = (By.CSS_SELECTOR, '[type="submit"]')

    def click_sign_in_page(self):
        self.click('SIGN_IN_PAGE')









