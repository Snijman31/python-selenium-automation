from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


Scenario: User can search for a product
Given Open target main page
When Search for soda
Then Verify search results shown


@given('Open target main page')
def open_main(context):
 context.driver.get('https://www.target.com/')

@when('Search for soda')
def search_product(context):
     context.driver.find_element(By.ID,'search').send_keys('soda')
     context.driver.find_element(By.XPATH,'//button[@data-test=@web/Search')





@then('Verify search results shown')
def verify_search_results(context):
    expected_result ='tea'
    actual_result = context.driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
    assert expected_result in actual_result