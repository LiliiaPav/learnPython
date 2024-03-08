from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/droppable/')

driver.switch_to.frame(0)

action_chains = ActionChains(driver)
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
time.sleep(4)

action_chains.drag_and_drop_by_offset (source, 100, 100).perform()
time.sleep(4)

action_chains.drag_and_drop(source, target).perform()
time.sleep(4)

driver.close()