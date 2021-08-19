
#explecit works with condition
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')

#this will maximize the window
#driver.maximize_window()

#path of website
driver.get('https://www.expedia.com/')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a/span').click()
time.sleep(5)

#one_way
driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/div/li[2]/a').click()
driver.implicitly_wait(5)


#source
driver.find_element_by_class_name('uitk-faux-input').click()
driver.implicitly_wait(5)

driver.find_element_by_class_name('uitk-faux-input').send_keys('Leaving from Bengaluru (BLR - Kempegowda Intl.)')
driver.implicitly_wait(5)

driver.find_element_by_class_name("uitk-field-input uitk-typeahead-input  ").\
    send_keys("Going to New York (NYC - All Airports)")

driver.implicitly_wait(4)