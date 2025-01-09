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

driver.find_element(By.CSS_SELECTOR,'[aria-label="Amazon"]')
driver.find_element(By.XPATH,"//input[@type='email']")
driver.find_element(By.ID,'continue')
driver.find_element(By.CSS_SELECTOR, '[aria-live="polite"]')
driver.find_element(By.CSS_SELECTOR,'aria-live="polite"')
driver.find_element(By.XPATH,"//*[@role='button']")
driver.find_element(By.ID,'auth-fpp-link-bottom')
driver.find_element(By.ID,'ap-other-signin-issues-link')
driver.find_element(By.ID,'createAccountSubmit')