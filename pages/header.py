from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage


class Header(BasePage):
   SEARCH_FIELD = (By.XPATH,'//input[@data-test="@web/Search/SearchInput"]')
   SEARCH_BTN = (By.XPATH,"//button[@data-test='@web/Search/SearchButton']")
   CART_ICON = (By.XPATH, '//a[contains(@href, "/cart") and @data-test="@web/CartLink"]')


   def search_products(self):
     self.input_text('juice',*self.SEARCH_FIELD)
     self.click(*self.SEARCH_BTN)



   def click_cart_icon(self):
       sleep(2)
       self.click(*self.CART_ICON)

