__author__ = 'leihuang'

def minValue():
    print "in func"
    current = yield
    print "after first yield"
    while True:
        print "in while before yield, current=%d" %current
        value = yield current
        print "in while after yield, current=%d, value=%d" %(current,value)
        current = min(value,current)

it = minValue()
print "before first next"
next(it)
print "after first next"
a = it.send(10)
print "a=%d" %a
b = it.send(4)
print "b=%d" %b

print "================"

def delegated():
    yield 1
    yield 2

def composed():
    yield 'A'
    for value in delegated():
        yield value
    yield 'B'

print list(composed())

print "================"

class MyReturn(Exception):
    def __init__(self, value):
        self.value = value

def delegated():
    yield 1
    raise MyReturn(2)
    yield "Not reached"

def composed():
    try:
        for value in delegated():
            yield value
    except MyReturn as e:
        output = e.value
    yield output*4

print list(composed())