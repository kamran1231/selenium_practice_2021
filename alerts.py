'''
Working with alerts
1- switch_to_alert().accept()
2- switch_to_alert().dismiss()
'''
import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://testautomationpractice.blogspot.com/')

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

time.sleep(4)
#popup boxes

alert_obj = driver.switch_to.alert

#use to accept the alert
alert_obj.accept()

#use to cancel the alert
#alert_obj.dismiss()

time.sleep(3)
driver.close()