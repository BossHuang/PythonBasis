__author__ = 'leihuang'

import sys
if sys.platform.startswith('win32'):
    print sys.platform," do something in if"
else:
    print sys.platform, " do something in else"
