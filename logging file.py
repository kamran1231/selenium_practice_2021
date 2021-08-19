
'''
Logging and Log Level

Logging is a very useful tool in a programmer toolbox. it can help u develop  a better  understanding
of the flow of a program and discover scenarios that you might not even have thought of while
developing.

Log Level
-DEBUG
-INFO
-WARNING
-ERROR
-CRITICAL
-
'''

import logging

logging.basicConfig(filename="C://Users//khanb//PycharmProjects//selenium//selenium_log//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG) #it will display all type of debug




logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is warning message')
logging.error('this is error message')
logging.critical('this is critical message')