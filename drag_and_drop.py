
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

driver.maximize_window()


source_ele = driver.find_element_by_xpath('//*[@id="box6"]')
dest_ele = driver.find_element_by_xpath('//*[@id="box106"]')

action = ActionChains(driver)

action.drag_and_drop(source_ele,dest_ele).perform()