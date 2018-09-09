__author__ = 'leihuang'

import __main__
if __main__.TESTING:
    print "do something in if %s " % __main__.TESTING
else:
    print "do something in else %s" % __main__.TESTING