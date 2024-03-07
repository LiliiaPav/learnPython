from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Locator strategy: is a way of finding an element 
try:
    driver.get('https://the-internet.herokuapp.com/')
    driver.find_element(By.LINK_TEXT, 'Form Authentication')
    els= driver.find_elements(By.TAG_NAME, 'a')
    print(f' There are {len(els)} anchor elements')

    els= driver.find_elements(By.TAG_NAME, 'foo')
    print(f' There are {len(els)} foo elements')
finally:
    driver.quit()








