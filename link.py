from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('http://demo.guru99.com/test/newtours/index.php')


link = driver.find_elements(By.TAG_NAME,"a")

#print how many links present in the page
print("No. of links present:",len(link))

for l in link:
    print(l.text)

driver.implicitly_wait(5)



#driver.find_element(By.LINK_TEXT,'REGISTER').click()

#partial_text
driver.find_element(By.PARTIAL_LINK_TEXT,'REG').click()