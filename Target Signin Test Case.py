from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get('https://www.target.com/')
sleep(2)

# Search
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
sleep(2)
driver.find_element(By.XPATH,"//*[@data-test='accountNav-signIn']").click()

sleep(5)

# Verification:
expected_result = "Sign into your Target account"
actual_result = driver.find_element(By.XPATH, "//h1/span").text
assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'



# Verify an element present:
driver.find_element(By.ID, 'login')


