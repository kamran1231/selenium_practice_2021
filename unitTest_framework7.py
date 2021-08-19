'''
assertIsNone -
assertIsNone method verifies whether give values or expression results in None or not, if the result is
none then python unittest will pass the test case otherwise fails the testcase


assertIsNotNone -
assertIsNotNone method verifies whether given values is not None, if the value is None then the test case
will be failed
'''

import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path='chromedriver.exe')

        self.assertIsNone(driver)
        # driver.get('https://google.com/')
        # titleOfWebPage = driver.title



if __name__ == '__main__':
    unittest.main()