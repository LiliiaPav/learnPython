from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
try:
    driver.get('http://wiki.python.org/moin/FrontPage')
    time.sleep(2)
    search = driver.find_element(By.ID, 'searchinput')
    search.send_keys("Begginers")
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    rawText = Select(driver.find_element(By.XPATH, '//form[@class="actionsmenu"]/div/select[@name="action"]'))
    rawText.select_by_index(1)
    time.sleep(5)

finally:
    driver.quit()