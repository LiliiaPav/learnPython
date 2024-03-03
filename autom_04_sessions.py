import time
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get('https://the-internet.herokuapp.com/')
    time.sleep(5)


finally:
    driver.quit()








