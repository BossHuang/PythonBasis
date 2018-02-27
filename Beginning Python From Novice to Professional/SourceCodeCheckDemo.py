__author__ = 'leihuang'

import unittest, doctest_demo
from subprocess import Popen, PIPE

class SquareTestCase(unittest.TestCase):

    def testNumber(self):
        for i in range(4):
            result = doctest_demo.square(i)
            self.failUnless(i*i==result, 'Error')

    def testWithPyChecker(self):
        cmd = 'pychecker', '-Q', doctest_demo.__file__.rstrip('c')
        pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pychecker.stdout.read(), '')

    def testWithPylint(self):
        cmd = 'pylint', '-rn', 'doctest_demo'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(), '')

if __name__ == '__main__':
    unittest.main()