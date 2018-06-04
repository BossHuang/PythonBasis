__author__ = 'leihuang'

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print meta, name, bases, class_dict
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object):
    __metaclass__ = Meta
    stuff = 123
    def foo(self):
        pass

print "----------------------"

class ValidateIntNumber(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict['value'] < 0:
                raise ValueError("value must be > 0")
        return type.__new__(meta, name, bases, class_dict)

class Number(object):
    __metaclass__ = ValidateIntNumber
    value = None

print "before class"
class IntNumber(Number):
    print "before value"
    value = 5
    print "after value"
print "after class"


