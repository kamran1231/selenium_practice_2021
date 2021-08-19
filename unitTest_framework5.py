

'''
Assertion is nothing  but the check point or u can say it as verification for tbe test case to evaluate
some item on the execution.

if we do not provide any assertion inside the test case then is no way to know whether a test case
failed or not

Assertion helps in report generation based on the assertion the test execution report will be generated


there are few assertion which will accept all the values and few assertion will accept only numeric
values


assertEqual-
assertEqual compare the first parameter with the second parameter with the second parameter,if both
matches the unittest will continue with the remaining execution but the both the values are different
then test fails the testcase


assertNotEqual-
assertNotEqual method compares the given two parameters, if both parameter are not same
then unittest passes the test case but if both parameter are same then unittest fails the test case.

'''

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get('https://www.google.com/')
        titleOfWebPage = driver.title


        #assertEqual
        #self.assertEqual("Google123",titleOfWebPage,'webpage title is not same')
        self.assertNotEqual('Google121',titleOfWebPage)


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()










