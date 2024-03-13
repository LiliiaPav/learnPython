from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get('http://sbasu.pythonanywhere.com/tastyFoodApp/')
    element = driver.find_element(By.LINK_TEXT, 'Create New Profile')
    element.click()
    time.sleep(5)
finally:
    driver.quit()