
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.selenium.dev/documentation/')
print(driver.title)
time.sleep(5)
#driver.maximize_window()
#driver.minimize_window()
driver.get('https://www.javatpoint.com/selenium-tutorial')
var = driver.find_element_by_class_name('gsc-input')
print(var.is_displayed())

var = driver.find_element_by_name('search')
print(var.is_enabled())
print(driver.title)
#print(driver.page_source)

driver.back()
print(driver.title)

driver.forward()



driver.quit()