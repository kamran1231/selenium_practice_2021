import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#chrome
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.w3schools.com/js/DEFAULT.asp')

#title
print(driver.title)

#url
print(driver.current_url)

#xpath
driver.find_element_by_xpath('//*[@id="main"]/div[2]/a[2]').click()

time.sleep(5)

#driver.close()  #currently focused browser

driver.quit()  #close all tab browser
