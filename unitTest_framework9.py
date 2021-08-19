



'''
assertIn-
method verifies whether the first element is present in the send element. if first element is present
in second element then test passed otherwise test is failed.

assertNotIn-
method verifies whether the first element is not present in the second element or not present in the
second element or not, if first element is present then test will be failed otherwise test is passed


These two methods will be helpful when you want to verify presence of a value in a list,tuple,set and
dictionary
'''


import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        #assert greater
        #self.assertGreater(100,10)
        #self.assertGreaterEqual(100,100)
        #self.assertLess(10,100)
        self.assertLessEqual(90,100)


if __name__ == '__main__':
    unittest.main()
