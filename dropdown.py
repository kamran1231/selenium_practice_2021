
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


s = Service('chromedriver.exe')
driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get('https://www.facebook.com/')


#driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("\\a[text()='Create New Account']").click()

