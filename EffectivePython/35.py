__author__ = 'leihuang'

class Field(object):
    def __init__(self, name):
        print "In Field init"
        self.name = name
        self.internal_name = '_'+self.name

    def __get__(self, instance, instance_type):
        print "In Field __get__"
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        print "In Field __set__"
        setattr(instance, self.internal_name, value)

class Customer(object):
    first_name = Field('first_name')
    last_name = Field('last_name')

foo = Customer()
print "----"
print "before: ", foo.first_name, foo.__dict__
print "----"
foo.first_name = 'x'
print "----"
print "after: ", foo.first_name, foo.__dict__

print "=============="

class Field(object):
    def __init__(self):
        print "in Field __init__"
        self.name = None
        self.internal_name = None

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print "In Meta"
        print meta, name, bases, class_dict
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_'+key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls

class DatabaseRow(object):
    __metaclass__ = Meta
    print "In DatabaseRow"

class Customer(DatabaseRow):
    first_name = Field()
    last_name = Field()

foo = Customer()
print "----"
print "before: ", foo.first_name, foo.__dict__
print "----"
foo.first_name = 'x'
print "----"
print "after: ", foo.first_name, foo.__dict__