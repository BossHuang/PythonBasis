__author__ = 'leihuang'

class Person():

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "I'm %s" % self.name

man = Person()
man.setName("L")
man.greet()
print man.name

class PrivateDemo():
    def __in(self):
        print "in"
    def out(self):
        print "out"
        self.__in()

s = PrivateDemo()
s.out()
#s.__in()

class MemberCount():
    members = 0
    def init(self):
        MemberCount.members += 1

m1 = MemberCount()
m1.init()
print MemberCount.members
m2 = MemberCount()
m2.init()
print MemberCount.members
m1.members = "T"
print m1.members
print m2.members

class Father():
    def init(self):
        pass
    def do(self):
        pass

class Mother():
    def init(self):
        pass
    def say(self):
        pass

class Sun(Father, Mother):
    pass

print issubclass(Sun, Father)
print issubclass(Father, Sun)
print issubclass(Mother, Father)

print Sun.__bases__

s = Sun()
print isinstance(s, Sun)
print s.__class__

sun = Sun()
print hasattr(sun,'say')
print hasattr(sun, 'look')
print callable(getattr(sun,'say'))
print hasattr(getattr(sun, 'say'), '__call__')

class A:
    def __init__(self, v = 2):
        self.value = v
    def hello(self):
        print "A"
        print self.value

class B(A):
    def __init__(self, n = 1):
        A.__init__(self, 3)
        self.num = n
b = B()
b.hello()

class A(object):
    def __init__(self, v = 2):
        self.value = v
    def hello(self):
        print "A"
        print self.value

class B(A):
    def __init__(self, n = 1):
        super(B, self).__init__(3)
        self.num = n
b = B()
b.hello()

def checkIndex(key):
    if not isinstance(key, (int, long)):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence:
    def __init__(self, start = 0, step = 2):
        self.start = start
        self.step = step
        self.changed = {}
    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step
    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value

s = ArithmeticSequence(2, 3)
print s[1]

class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.count = 0
    def __getitem__(self, index):
        self.count += 1
        return super(CounterList, self).__getitem__(index)
c = CounterList(range(3))
print c[0]
print c.count

__metaclass__ = type
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

r = Rectangle()
r.size = (5,6)
print r.width, r.height
r.width = 7
print r.size

__metaclass__ = type
class A:
    def sm():
        print "static method"
    sm = staticmethod(sm)
    def cm(cls):
        print "class method"
    cm = classmethod(cm)

A.cm()
A.sm()

__metaclass__ = type
class A:
    @staticmethod
    def sm():
        print "static method"

    @classmethod
    def cm(cls):
        print "class method"

A.cm()
A.sm()

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, key, value):
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value
    def __getattr__(self, item):
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError

r = Rectangle()
print r.size

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 10:
        print f
        break

it = iter([1,2,3])
print it.next()
print it.next()

class TestIterator:
    def __init__(self):
        self.v = 0
    def next(self):
        self.v += 1
        if self.v > 5:
            raise StopIteration
        return self.v
    def __iter__(self):
        return self

tt = TestIterator()
print list(tt)

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
a = [[1,2],[3,4]]
print flatten(a)
print list(flatten(a))

r = (i for i in range(5))
print r
print r.next()
print sum(i for i in range(10))

def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new
r = repeater(42)
print r.next()
print r.send("hello")