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




