import time
from selenium import webdriver


options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.get('file:///Users/liliiapavliuchenkova/Documents/learnPython/html_code_02.html')

#find an element by id
# login_form=driver.find_element('id', 'loginForm')
# print("My login form element is: ", login_form)

#find an element by name
# username=driver.find_element('name', 'username')
# print("My username element is: ", username)

#absolute xPath
login_form_abs=driver.find_element('xpath', '/html/body/form[1]')
#relative
login_form_rel=driver.find_element('xpath', '//form[1]')

#by id
login_form_id=driver.find_element('xpath', '//form[@id="loginForm"]')

print("My absolute path element is: ", login_form_abs)
print("My relative path element is: ", login_form_rel)
print("My id path element is: ", login_form_id)

time.sleep(5)

driver.close()



# time.sleep(15)

