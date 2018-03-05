__author__ = 'leihuang'

import math
x = 1
y = math.sqrt
print callable(x)
print callable(y)

def square(x):
    'Calculate the square of x.'
    return x*x

print square.__doc__
help(square)

def addOne(x):
    x += 1
x = 3
addOne(x)
print x

def addOne(x):
    x[0] += 1
x = [1,2]
addOne(x)
print x

def export(x, y = 2, *z, **n):
    print x
    print y
    print z
    print n

export(1, 2, 3, 4, t = 2)
export(1)

def cal1(x,y):
    print x+y
def cal2(x=1,y=2):
    print x+y
par1 = (3,4)
cal1(*par1)
par2 = {'x':5,'y':1}
cal2(**par2)

def addOne(y):
    print y+globals()['x']

    global x
    x += 1
    print x
    print y

x = 2
scope = vars()
print scope['x']

addOne(x)

def addX(x):
    def addY(y):
        return x+y
    return addY

print map(str, range(3))

def func(x):
    if x > 1:
        return True
    return False

print filter(func, range(3))

print reduce(lambda x,y:x+y,range(3))