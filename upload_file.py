
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://testautomationpractice.blogspot.com/')

driver.switch_to.frame(0)

driver.find_element_by_id("RESULT_FileUpload-10").send_keys('D://images/B612_20200815_000533_481.jpg')