__author__ = 'leihuang'

a = [1,2,3,4]
a_odds = a[::2]
a_evens = a[1::2]
print a_odds
print a_evens

x = b'message'
y = x[::-1]
print y

from itertools import islice
a = [1,2,3,4]
b = islice(a, 1,4,2)
print b
print list(b)