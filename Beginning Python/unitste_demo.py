__author__ = 'leihuang'

import doctest_demo, unittest

class SquareTestCase(unittest.TestCase):
    def testNumber(self):
        for i in range(4):
            result = doctest_demo.square(i)
            self.failUnless(i*i==result, 'Error')

if __name__ == '__main__':
    unittest.main()