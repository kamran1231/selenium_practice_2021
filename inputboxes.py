
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://forms.app/auth/signup')

driver.implicitly_wait(4)


#how many inputboxes present in webpage
input_boxes = driver.find_elements(By.CLASS_NAME,'f-input')

print(len(input_boxes))
driver.implicitly_wait(4)

#how to provide the value into the text box

driver.find_element(By.NAME,'full-name').send_keys("kamran")
driver.implicitly_wait(4)

driver.find_element(By.NAME,'email').send_keys("kamranmohd01@gmail.com")
driver.implicitly_wait(4)

driver.find_element(By.NAME,'username').send_keys("kamran12")
driver.implicitly_wait(4)

driver.find_element(By.NAME,'password').send_keys("iamthebest12")
driver.implicitly_wait(4)

driver.find_element(By.NAME,'confirm-password').send_keys("iamthebest12")
driver.implicitly_wait(4)

driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[1]/div[2]/form/div[6]/div/label/span/i').click()
driver.implicitly_wait(4)

driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[1]/div[2]/form/div[8]/div').click()
driver.implicitly_wait(4)