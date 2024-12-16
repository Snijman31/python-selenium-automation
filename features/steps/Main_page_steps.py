from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
 context.driver.get('https://www.target.com/')
sleep(5)


@when('Search for soda')
def search_product(context):
     context.driver.find_element(By.ID,'search').send_keys('soda')
     context.driver.find_element(By.XPATH,'//button[@data-test=@web/Search')


