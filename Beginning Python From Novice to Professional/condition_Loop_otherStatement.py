__author__ = 'leihuang'

print 1,3,
print 2

x, y, z = 1,2,3
print x,y,z

y, x = x, y
print x, y, z

# x, y, *z = [1,2,3,4]
# print x,y,z

# x = y = somefunction()
#
# y = somefunction()
# x = y
#
# x = somefunction()
# y = somefunction()

x = y = [1,2,3]
z = [1,2,3]
print x == y
print x == z
print x is y
print x is z

#a = -1
#assert 1 < a < 10, "out of range"

x = {1:2,2:3}
for key, value in x.items():
    print key, value

for key, value in x.iteritems():
    print key, value

x = [1,2,3]
y = [6,7,8]
print zip(x,y)
for i,j in zip(x,y):
    print i,j
y = [6,7]
print zip(x,y)

x = [6,7]
print enumerate(x)
for index, value in enumerate(x):
    print index, value

x = [1,3,2]
print sorted(x)
print reversed(x)

print [(x,y) for x in range(3) for y in range(3) if x == y]

x = [1,2]
y = x
print x,y
del x
print y
# print x

# from math import sqrt
# exec "sqrt = 1"
# print sqrt
# print sqrt(4)

from math import sqrt
scope = {}
exec "sqrt = 1" in scope
print scope['sqrt']
print sqrt(4)

print len(scope)
print scope.keys()

print eval("3+2")

scope = {}
scope['x'] = 1
scope['y'] = 2
print eval('x+y', scope)

scope = {}
exec 'x=2' in scope
print eval('x+1', scope)

