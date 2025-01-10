from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage


class Header(BasePage):
   SEARCH_FIELD = (By.XPATH,'//input[@data-test="@web/Search/SearchInput"]')
   SEARCH_BTN = (By.XPATH,"//button[@data-test='@web/Search/SearchButton']")
   CART_ICON = (By.XPATH, '//a[contains(@href, "/cart") and @data-test="@web/CartLink"]')
   SIGN_IN = (By.CSS_SELECTOR,'[data-test="@web/AccountLink"]')

   def search_products(self,product):
     self.input_text(product,*self.SEARCH_FIELD)
     self.click(*self.SEARCH_BTN)



   def click_cart_icon(self):
       sleep(2)
       self.wait_and_click(*self.CART_ICON)

   def click_sign_in(self):
       self.wait_and_click(*self.SIGN_IN)


