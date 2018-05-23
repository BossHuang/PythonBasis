__author__ = 'leihuang'

class BaseClass(object):
    def __init__(self, value):
        self.value = value
        print "In BaseClass ", self.value

class ChildClass(BaseClass):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        print "In Child ", self.value

#c = ChildClass(5)

#=========================================

class TimeTwo(object):
    def __init__(self):
        self.value *= 2
        print "In TimeTwo ", self.value

class PlusFive(object):
    def __init__(self):
        self.value += 5
        print "In PlusFive ", self.value

class One(BaseClass, TimeTwo, PlusFive):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        TimeTwo.__init__(self)
        PlusFive.__init__(self)
        print "In One ", self.value

print "--------- one ----------"
one = One(5)

class Two(BaseClass, PlusFive, TimeTwo):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        TimeTwo.__init__(self)
        PlusFive.__init__(self)
        print "In Two ", self.value

print "--------- two ----------"
two = Two(5)

#=========================================

class TimeTwo_v2(BaseClass):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        self.value *= 2
        print "In TimeTwo_v2 ", self.value

class PlusFive_v2(BaseClass):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        self.value += 5
        print "In PlusFive_v2 ", self.value

class Three(TimeTwo_v2, PlusFive_v2):
    def __init__(self, value):
        TimeTwo_v2.__init__(self, value)
        PlusFive_v2.__init__(self, value)
        print "In Three ", self.value

print "--------- three ----------"
three = Three(5)

#=========================================

class TimeTwo_v3(BaseClass):
    def __init__(self, value):
        super(TimeTwo_v3, self).__init__(value)
        self.value *= 2
        print "In TimeTwo_v3 ", self.value

class PlusFive_v3(BaseClass):
    def __init__(self, value):
        super(PlusFive_v3, self).__init__(value)
        self.value += 5
        print "In PlusFive_v3 ", self.value

class Four(TimeTwo_v3, PlusFive_v3):
    def __init__(self, value):
        super(Four, self).__init__(value)
        print "In Four ", self.value

print "--------- four ----------"
four = Four(5)
print Four.mro()

class Five(PlusFive_v3, TimeTwo_v3):
    def __init__(self, value):
        super(Five, self).__init__(value)
        print "In Five ", self.value

print "--------- five ----------"
five = Five(5)
print Five.mro()
