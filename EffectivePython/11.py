__author__ = 'leihuang'

a = ['a','b','c']
b = [1,2,3,4]
c = ['x','y','z']
print zip(a,b,c)

from itertools import izip
a = ['a','b','c']
b = [1,2,3,4]
c = ['x','y','z']
print izip(a,b,c)

from itertools import izip_longest
a = ['a','b']
b = [1,2,3,4]
print list(izip_longest(a,b))