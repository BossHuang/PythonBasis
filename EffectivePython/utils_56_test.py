__author__ = 'leihuang'

from utils_56 import to_str
from unittest import TestCase, main

class UtilsTestCase(TestCase):
    def setUp(self):
        print "in setUp"
    def tearDown(self):
        print "in tearDown"
    def test_to_str_bytes(self):
        print "in test_to_str_bytes"
        self.assertEqual('hello', to_str('hello'))
    def test_to_str_str(self):
        print "in test_to_str_str"
        self.assertEqual('hello', to_str('hello'))
    def test_to_str_bad(self):
        print "in test_to_str_bad"
        self.assertRaises(TypeError, to_str, object)

if __name__ == '__main__':
    main()