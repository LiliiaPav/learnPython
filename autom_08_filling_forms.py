from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('file:///Users/liliiapavliuchenkova/Documents/learnPython/html_code_03_02.html')

select = Select(driver.find_element(By.NAME, 'numReturnSelect'))
select.select_by_index(4)
time.sleep(5)
select.select_by_visible_text('200')
time.sleep(5)
select.select_by_value('250')
time.sleep(5)

options = select.options
print(options)

submit_button = driver.find_element(By.NAME, 'continue')
submit_button.submit()
time.sleep(5)

driver.quit()
'''

    select_element = driver.find_element(By.NAME, 'selectomatic')
    select = Select(select_element)

    two_element = driver.find_element(By.CSS_SELECTOR, 'option[value=two]')
    four_element = driver.find_element(By.CSS_SELECTOR, 'option[value=four]')
    count_element = driver.find_element(By.CSS_SELECTOR, "option[value='still learning how to count, apparently']")

    select.select_by_visible_text('Four')
    assert four_element.is_selected()

    select.select_by_value('two')
    assert two_element.is_selected()

    select.select_by_index(3)
    assert count_element.is_selected()

'''