import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('http://demo.guru99.com/test/newtours/index.php')


ele = driver.find_element_by_name('userName')

print(ele.is_displayed())  #return true/false based of element status
print(ele.is_enabled())  #return true/false


ele_psw = driver.find_element_by_name('password')

print(ele.is_displayed())
print(ele.is_enabled())

ele.send_keys('mercury')
ele_psw.send_keys('mercury')


driver.find_element_by_name('submit').click()

time.sleep(5)


driver.get('http://demo.guru99.com/test/newtours/reservation.php')
#agr input m value h to css_selector use krenge
rountrip_radio = driver.find_element_by_css_selector("input[name=tripType]")


print("status of round trip radio button is",rountrip_radio.is_selected()) #return status of radio round button

one_way_btn = driver.find_element_by_css_selector("input[value=oneway]")

print("status of oneway button is",one_way_btn.is_selected())

driver.close()