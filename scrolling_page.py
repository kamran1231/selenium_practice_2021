import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.worldometers.info/geography/flags-of-the-world/')

driver.maximize_window()

#1- Scroll down page by pixel
#driver.execute_script('window.scrollBy(0,4000)',"")

#2- Scroll down the page till the element is visible
#flag = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/div/div[123]/div/div')
#driver.execute_script("arguments[0].scrollIntoView();",flag)


#3 scroll down page till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(3)