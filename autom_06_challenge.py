from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://www.selenium.dev/')

    #find all ids on the page
    # ids=driver.find_elements(By.XPATH, '//*[@id]')
    # for i in ids:
    #     print (i.get_attribute('id'))


    #find by id
    # els= driver.find_element(By.CSS_SELECTOR, '#td-block-0')
    # print(els)

    #find all names on the page
    # names=driver.find_elements(By.XPATH, '//*[@name]')
    # for i in names:
    #     print (i.get_attribute('name'))

    #find an element by its name
    # submit= driver.find_element(By.NAME, 'submit')
    # print(submit)

    # seleniumHeading=driver.find_element(By.XPATH, '//main/section/div/div/div/h1')

    #find all classes on the page and sort them
    # classes=driver.find_elements(By.XPATH, '//*[@class]')
    # classes2=[]
    # for i in classes:
    #     classes2.append(i.get_attribute('class'))
        
    # classes2.sort()
    # for i in classes2:
    #     print(i)
    content=driver.find_element(By.CLASS_NAME, 'selenium')
    print(content)

finally:
    driver.quit()
