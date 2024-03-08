from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get('http://python.org/')
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'start-shell'))
    )
    print(element)
finally:
    driver.quit()