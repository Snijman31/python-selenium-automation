from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage
SIDE_NAV_SIGN_IN = (By.CSS_SELECTOR,'[data-test="accountNav-signIn"]')

class SideSignInPage(BasePage):
    def side_nav_sign_in(self):
        self.click(SIDE_NAV_SIGN_IN)

