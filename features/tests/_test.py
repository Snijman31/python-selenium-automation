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

driver.find_element(By.CSS_SELECTOR,'.a-link-nav-icon')
driver.find_element(By.CSS_SELECTOR,'.a-spacing-small')
driver.find_element(By.ID,"ap_customer_name")
driver.find_element(By.ID,'ap_email')
driver.find_element(By.ID,'ap_password')
driver.find_element(By.ID,'ap_password_check')
driver.find_element(By.ID,'continue')
driver.find_element(By.CSS_SELECTOR,'.a section a spacing-extra-large')
driver.find_element(By.CSS_SELECTOR,'.a-link-emphasis')



