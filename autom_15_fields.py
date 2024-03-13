from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get('http://sbasu.pythonanywhere.com/tastyFoodApp/')
    element = driver.find_element(By.LINK_TEXT, 'Create New Profile')
    element.click()
    first_name=driver.find_element(By.ID, 'id_firstName')
    first_name.send_keys('Kia')
    last_name=driver.find_element(By.ID, 'id_lastName')
    last_name.send_keys('Taco')
    driver.find_element(By.ID, 'id_gender_1').click()
    user_name=driver.find_element(By.ID, 'id_username')
    user_name.send_keys('KiaTaco')
    password= driver.find_element(By.ID, 'id_password')
    password.send_keys('Kia23')
    state = Select(driver.find_element(By.ID, 'id_state'))
    state.select_by_visible_text('Texas')
    fee=Select(driver.find_element(By.ID, 'id_fee'))
    fee.select_by_visible_text('$150 : Gold')
    time.sleep(5)
finally:
    driver.quit()







