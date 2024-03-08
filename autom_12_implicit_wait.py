from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.implicitly_wait(10)
    driver.get('http://python.org/')
    element = driver.find_element(By.ID, 'start-shell')
    print(element)
finally:
    driver.quit()