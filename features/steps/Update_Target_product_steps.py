from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.XPATH,'//input[@data-test="@web/Search/SearchInput"]')
SEARCH_BTN =(By.XPATH,"//button[@data-test='@web/Search/SearchButton']")



#@given('Open target main page')
#def open_main(context):
#    context.app.main_page.open_main()


#@when('Search for juice')
#def search_juice(context):
#    context.app.header.search_products('juice')


#@then('Verify search results shown juice')
#def verify_search_results(context):
#    context.app.search_results_page.verify_search_results('juice')

#@then('Verify search term {product} in URL')
#def verify_search_results_search_url(context,product):
#    context.app.search_results_page.verify_search_url(product)

