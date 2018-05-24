__author__ = 'leihuang'

class Parent(object):
    def __init__(self):
        self.__value = 5

    @classmethod
    def get_private_value_of_instance(cls, instance):
        return instance.__value

p = Parent()
print Parent.get_private_value_of_instance(p)

class Child(Parent):
    def get_private_value(self):
        return self.__value

c = Child()
print c.__dict__

#=======================
class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)

class IntegerClass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)

vv = IntegerClass(3)
print vv.get_value()

class BaseClass(object):
    def __init__(self, value):
        self.__value = value
    def get_value(self):
        return self.__value

 #class MyClass(BaseClass):
 #    pass

#=====================================

class ApiClass(object):
    def __init__(self):
        self._value = 5
    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super(Child, self).__init__()
        self._value = 'hello'

c = Child()
print c.get(),c._value

#============================
class ApiClass(object):
    def __init__(self):
        self.__value = 5
    def get(self):
        return self.__value

class Child(ApiClass):
    def __init__(self):
        super(Child, self).__init__()
        self._value = 'hello'

c = Child()
print c.get(),c._value