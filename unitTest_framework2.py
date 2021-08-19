
import unittest

from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.google.com/')
        print('the title of the page is:',self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.bing.com/')
        print('the title of the page is:', self.driver.title)
        self.driver.close()
if __name__ == '__main__':
    unittest.main()