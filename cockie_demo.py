
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.amazon.in/')

#capture all the cockies by browser
cockies = driver.get_cookies()
print(len(cockies))  #print number of cockies have been created

print(cockies)

#Adding new cookie to the browser

cookie = {'name':'myCookie','value':'123585984'}

driver.add_cookie(cookie)

d = driver.get_cookies()
print(len(d))
print(d)

#Deleting cookie
driver.delete_cookie('myCookie')
cookie = driver.get_cookies()
print(len(cookie))
print(cookie)


#Deleting all cookie
driver.delete_all_cookies()
cockies = driver.get_cookies()
print(cockies)