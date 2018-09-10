__author__ = 'leihuang'

print "1"
print 1

a = "x"
print repr(a)
b = eval(repr(a))
print a is b

print repr("5")
print repr(5)
print "%r" % 5
print "%r" % '5'

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = Point(1,2)
print p1

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point(%d,%d)' %(self.x, self.y)
p1 = Point(1,2)
print p1.__dict__