
'''
Skipping tests
1- skip test
2- skip test with reason
3- skip test with based on condition
'''

import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print('this is search test')

    @unittest.skip('i am skipping this test method bcz it is not yet ready')
    def test_advanceSearch(self):
        print('this is advance search test')

    @unittest.skipIf(1==1,'One is equal to one')
    def test_prepaidRecharge(self):
        print('this is prepaid recharge')

    def test_postRecharge(self):
        print('this is post recharge')

    def test_loginbygmail(self):
        print('this is login by email')

    def test_loginbytwitter(self):
        print('this is login by twitter')


if __name__ == '__main__':
    unittest.main()