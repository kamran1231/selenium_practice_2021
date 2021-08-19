

'''
assertTrue & assertFalse

assertTrue-
when we have only two parameter we can use assertEqual method to check whether both are same or not,
but if we have more than two parameter comparing values with assertEqual method become more
difficult.

assertTrue methods check whether given parameter is true or not, if value is true then test is passed
otherwise test is failed

assertFalse-
this method compares whether given value or expression results in false or not.

if the result or value is false then unittest passes the testcase but if the result or value is true
then unittest fails the test case.
'''


import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get('https://google.com/')
        titleOfWebPage = driver.title

        #self.assertTrue(titleOfWebPage == 'Google123')
        self.assertFalse(titleOfWebPage == 'Google123')

if __name__ == '__main__':
    unittest.main()