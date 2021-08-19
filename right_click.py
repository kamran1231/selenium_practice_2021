
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')


btn = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
action = ActionChains(driver)

action.context_click(btn).perform()