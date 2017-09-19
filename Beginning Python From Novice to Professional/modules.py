__author__ = 'leihuang'

print "---"
import Hi
print "---"
import Hi
print "---"
Hi = reload(Hi)
print "---"

import Hi2
Hi2.Hello()

from HelloWrold import Hello
import HelloWrold.World

import copy
print [n for n in dir(copy) if not n.startswith('_')]
print copy.__all__

print copy.copy.__doc__
help(copy.copy)