__author__ = 'leihuang'

import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('Starting program')
logging.info('try to divide 1/0')
print 1/0
logging.info('End')