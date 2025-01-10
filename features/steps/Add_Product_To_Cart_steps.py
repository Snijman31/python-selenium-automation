from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




CART_ICON = (By.CSS_SELECTOR,"[id*=addToCartButton]")


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(3)

@when('Search for candy')
def search_for_candy(context):
    context.app.header.search_products(product='candy')
    sleep(2)


@when('Click on Add to Cart Button')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()
    sleep(2)

@when('Confirm Add to Cart from side Navigation')
def side_nav_click_add_to_cart(context):

    context.driver.find_element(By.CSS_SELECTOR,'[style="display: flex;"]').click()


@then('Verify Cart has 1 item ')
def verify_cart_has_item(context):
    context.app.search_results_page.verify_candy_add_to_cart()