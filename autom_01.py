import time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://liliiapav.github.io/Fall2023_COMM675/root/')
# time.sleep(15)

