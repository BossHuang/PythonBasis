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

print range.__doc__

import copy
print copy.__file__

a = set([1,2,3,4])
b = set([2,3,4,5])
print a.union(b)
print a | b

print a.intersection(b)
print a & b

print a.difference(b)
print a - b

print a.symmetric_difference(b)
print a ^ b

c = a & b
print c.issubset(a)
print c.issuperset(a)
print a.copy() is a
print a.copy() == a

a = set([1,2])
b = set([2,3])
a.add(frozenset(b))
print a

from heapq import *
data = [4,1,3,6]
heap = []
for num in data:
    heappush(heap, num)
print heap

heapify(data)
print data

from collections import deque
q = deque(range((3)))
q.append(5)
q.appendleft(6)
print q

print q.pop()
print q.popleft()
print q

q.rotate(1)
print q

q.rotate(-2)
print q

import time
print time.asctime()

import time
import random
timeBegin = time.mktime((2017, 1, 1, 0, 0, 0, -1, -1, -1))
timeEnd = time.mktime((2017, 7, 1, 0, 0, 0, -1, -1, -1))
randTime = random.uniform(timeBegin, timeEnd)
print randTime
print time.asctime(time.localtime(randTime))

a = [1,2,3,4]
print random.choice(a)
random.shuffle(a)
print a
print random.sample(a,2)
print a

import shelve
s = shelve.open('test.dat')
s['x'] = ['a','b']
print s['x']
s['x'].append('d')
print s['x']

import shelve
s = shelve.open('test.dat')
s['x'] = ['a','b']
print s['x']
temp = s['x']
temp.append('d')
s['x'] = temp
print s['x']


import re
text = "alpha. beta. .... gama delta"
print re.split('[. ]+', text)
print re.split('[. ]+', text, maxsplit=2)
print re.findall('[.?\-",]+', text)

print re.sub("a",'A',text)

import re
m = re.match(r'www\.(.)*\..{3}','www.baidu.com')
print m.group(1)
print m.start(1)
print m.end(1)
print m.span(1)
