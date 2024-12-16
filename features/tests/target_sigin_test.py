from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.ID,'account-sign-in').click()
    context.driver.find_element(By.XPATH,'//*[@data-test=accountNav-signIn]').click()
    sleep(1)

@then('Verify Sign In form opened ')
def verify_sign_in(context):
    context.driver.find_element(By.ID,'username').click()
    expected_result = ["sign- in form opened"]
    actual_results = context.driver.find_element(By.XPATH, '//*[@data-test=accountNav-signIn]').text
    assert expected_result in actual_results, f'Expected text {expected_result} not in actual {actual_results}'
