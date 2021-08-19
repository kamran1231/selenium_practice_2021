

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#this will change the path of our download
chromeOptions = Options()

chromeOptions.add_experimental_option('prefs',{'download.default_directory':'F:\Django Notes'})


driver = webdriver.Chrome('chromedriver.exe',options=chromeOptions)
driver.get('http://demo.automationtesting.in/FileDownload.html')


driver.find_element_by_xpath('//*[@id="textbox"]').send_keys('hi kamran where are you'
                                                             ' inshaAllah Allah will help you')

driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="createTxt"]').click() #generate file button
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="link-to-download"]').click()  #Download link

