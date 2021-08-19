
'''
Webdriver offers API to take screenshot of a webpage
1- save_screenshot('filename')
2- get_screenshot_as_file('filename')
'''

from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://demo.guru99.com/test/newtours/index.php')

driver.save_screenshot('F:\\homepage.png')


driver.get_screenshot_as_file('F:\\homepage2.png')
