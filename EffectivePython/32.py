__author__ = 'leihuang'

class LazyDB(object):
    def __init__(self):
        self.exists = 5
    def __getattr__(self, name):
        print "In LazyDB.__getattr__"
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

lz = LazyDB()
print "before: ", lz.__dict__
print "1. x: ", lz.x
print "1. after: ", lz.__dict__
print "2. x: ", lz.x
print "2. after: ", lz.__dict_

print "------------------------------"

class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print "In LoggingLazyDB.__getattr__"
        return super(LoggingLazyDB, self).__getattr__(name)

lldb = LoggingLazyDB()
print "before: ", lldb.__dict__
print "1. zz: ", lldb.zz
print "1. after: ", lldb.__dict__
print "2. zz: ", lldb.zz
print "2. after: ", lldb.__dict__

print "------------------------------"

class ValidatingDB(object):
    def __init__(self):
        self.exists = 5
    def __getattribute__(self, name):
        print "In ValidatingDB.__getattribute__, called %s" % name
        try:
            print "try"
            return super(ValidatingDB, self).__getattribute__(name)
        except AttributeError:
            print "except"
            value = "value for %s" % name
            setattr(self, name, value)
            return value

v = ValidatingDB()
print "before: ", v.__dict__
print "1. zz: ", v.zz
print "1. after: ", v.__dict__
print "2. zz: ", v.zz
print "2. after: ", v.__dict__

print "------------------------------"

lz = LazyDB()
print "before: ", lz.__dict__
print '1. abc is exists ? ', hasattr(lz, 'abc')
print "1. after: ", lz.__dict__
print '2. abc is exists ? ', hasattr(lz, 'abc')
print "2. after: ", lz.__dict__

print "------------------------------"

class DictionaryDB(object):
    def __init__(self, data):
        self._data = data
    def __getattribute__(self, name):
        data_dict = super(DictionaryDB, self).__getattribute__('_data')
        return data_dict[name]

print "------------------------------"

class SavingDB(object):
    def __setattr__(self, key, value):
        print "In SavingDB.__setattr__ (%s, %r)" %(key, value)
        super(SavingDB, self).__setattr__(key, value)

class LoggingSavingDB(SavingDB):
    def __setattr__(self, key, value):
        print "In LoggingSavingDB.__setattr__ (%s, %r)" %(key, value)
        super(LoggingSavingDB, self).__setattr__(key, value)

data = LoggingSavingDB()
print "before: ", data.__dict__
data.x = 1
print "1. after: ", data.__dict__
data.x = 2
print "2. after: ", data.__dict__
