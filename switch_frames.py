
'''Working with frames

1- switch_to.frame(name)
2- switch_to.frame(id)
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://testautomationpractice.blogspot.com/')



#alert
driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(3)

alert_obj = driver.switch_to.alert
alert_obj.accept()

time.sleep(4)


date_click = driver.find_element(By.ID,'datepicker')
date_click.send_keys('04/17/2021')

driver.implicitly_wait(3)

#select a speed
select_speed = driver.find_element(By.ID,'speed')
select_speed.send_keys('Fast')


#select a file
select_file = driver.find_element(By.ID,'files')
select_speed.send_keys('DOC file')

driver.implicitly_wait(3)

#select gender
driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[2]/td/label').click()
#btn.send_keys('Female')