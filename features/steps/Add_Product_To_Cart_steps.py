from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
     context.driver.get('https://www.target.com/')
sleep(2)

@when('Search for candy')
def search_for_candy(context):
    context.driver.find_element(By.XPATH, '//input[@data-test="@web/Search/SearchInput"]') .send_keys('candy')
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="@web/Search/SearchButton"').click()
    sleep(5)


@when('Click on Add to Cart Button')
def click_add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR,"[id*=addToCartButton]").click()
    sleep(3)


@when('Confirm Add to Cart from side Navigation')
def side_nav_click_add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR,'[style="display: flex;"]').click()
    sleep(3)

@then('Verify cart has 1 item')
def verify_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="modal-drawer-heading"]')