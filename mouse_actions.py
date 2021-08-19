
#Mouse Actions
# Mouse Hover
# Double click
# Right click
# Drag and drop
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#ActionChains are a way to automate low level interactions such as
# #mouse movements, mouse button actions, key press, and context menu interactions.
#This is useful for doing more complex actions like hover over and drag and drop.
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.seleniumeasy.com/tags/mouse-hover')

driver.implicitly_wait(5)
# alert_obj = driver.switch_to.alert
# driver.implicitly_wait(3)
# alert_obj.dismiss()
driver.find_element(By.CLASS_NAME,'dropdown-toggle').click()
driver.find_element(By.LINK_TEXT,'Selenium with Python').click()



