
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('http://demo.guru99.com/test/newtours/index.php')
#oprning url wait sometime

driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys('mercury')
driver.find_element_by_name("password").send_keys('mercury')
driver.find_element_by_name('submit').click()



driver.close()
