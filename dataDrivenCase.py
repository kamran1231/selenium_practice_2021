
import xutils

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('http://demo.guru99.com/test/newtours/')

driver.maximize_window()
print(driver.title)
path = 'C:\\Users\khanb\PycharmProjects\selenium\write_excel.xlsx'

rows = xutils.getRowCount(path,'Sheet1')

for i in range(2,rows):
    username = xutils.readData(path,'Sheet1',i,1)
    password = xutils.readData(path,'Sheet1',i,2)

    driver.find_element_by_name('userName').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('submit').click()

    if driver.title=='Login: Mercury Tours':
        print('test is passed')
        xutils.writeData(path,'Sheet1',i,3,'test passed')
    else:
        print('test failed')
        xutils.writeData(path,'Sheet1',i,3,'test failed')

    driver.find_element_by_link_text('Home').click()

driver.close()