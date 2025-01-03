from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given('Open target main page')
#def open_main(context):
 #  context.driver.get('https://www.target.com/')

#@when('Click cart icon')
#def click_cart_icon(context):
 #  context.driver.find_element(By.XPATH, '//*[@data-test=@web/CartLink"]').click()


#@then('Verify Your Cart is empty message is shown')
#def verify_your_cart_is_empty(context):
  #  expected_results = ['Your cart is empty']
 #   actual_results = context.driver.find_element(By.XPATH,'//div[@data-test=boxEmptyMsg]').text
   # assert expected_results in  actual_results, f'Expected text {expected_results} not in actual {actual_results}'