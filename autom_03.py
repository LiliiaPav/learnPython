import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.get('file:///Users/liliiapavliuchenkova/Documents/learnPython/html_code_02.html')

content=driver.find_element(By.CLASS_NAME, 'content')
print(content)
time.sleep(5)

driver.close()


