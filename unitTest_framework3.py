
'''
Python unitTest Framework
1- setup
2- teardown
3- setUpClass
4- tearDownClass
5- setUpModule
6- tearDownModule
'''


import unittest


#will executed before executing any class or any menthod
def setUpModule():
    print('setUpModule')

#will executed after the every present in the python module
def tearDownModule():
    print('tearDownModule')

class AppTesting(unittest.TestCase):
    #this will run in before every test
    @classmethod
    def setUp(self):
        print('this is login test')

    #this will run after the every test
    @classmethod
    def tearDown(self):
        print('this is logout test')

    #this method run only one time before all method started
    @classmethod
    def setUpClass(cls):
        print('open Application')

    #this method execute after the class completed
    @classmethod
    def tearDownClass(cls):
        print('close application')



    def test_search(self):
        print('this is search test')

    def test_advancedsearch(self):
        print('this is advanced search test')

    def test_prepaidRecharge(self):
        print('this is prepaid recharge test')

    def test_postpaidRecharge(self):
        print('this is post paidRecharge test')

if __name__ == '__main__':
    unittest.main()
