__author__ = 'leihuang'

from collections import deque
fifo = deque()
fifo.append(1)
x = fifo.popleft()
print x

print "============="

a = {}
a['x'] = 1
a['y'] = 2
c = {}
c['x'] = 1
c['y'] = 2
print a == c

from random import randint
while True:
    z = randint(99,1013)
    b = {}
    for i in range(z):
        b[i] = i
    b['x'] = 1
    b['y'] = 2
    for i in range(z):
        del b[i]
    if str(a) != str(b):
        print a
        print b
        print a == b
        break

print "============="

from collections import OrderedDict
a = OrderedDict()
a['x'] = 1
a['y'] = 2
b = OrderedDict()
b['x'] = 'xx'
b['y'] = 'yy'
for v_a, v_b in zip(a.values(), b.values()):
    print v_a,v_b

print "============="

key = 'x'
status = {}
if key not in status:
    status[key] = 0
status[key] += 1
print status

status = {}
status[key] = status.setdefault(key,0)+1
print status

from collections import defaultdict
status = defaultdict(int)
status[key] += 1
print status

print "============="

from collections import _heapq
a = []
_heapq.heappush(a, 5)
_heapq.heappush(a, 3)
_heapq.heappush(a, 7)
_heapq.heappush(a, 4)
print a

print "============="

import bisect
a = list(range(100))
i = bisect.bisect_left(a, 98)
print i

