__author__ = 'leihuang'

import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})

    @classmethod
    def deserialize(cls, json_data):
        param = json.loads(json_data)
        return cls(*param['args'])

class Point2D(Serializable):
    def __init__(self, x, y):
        super(Point2D, self).__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)

point = Point2D(1, 2)
print point
data = point.serialize()
print data
p2 = Point2D.deserialize(data)
print p2

print '----------------------'

class Serializable_v2(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'class': self.__class__.__name__, 'args': self.args})

registry = {}
def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class Point2D(Serializable_v2):
    def __init__(self, x, y):
        super(Point2D, self).__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)

register_class(Point2D)

p1 = Point2D(2, 3)
print p1
data = p1.serialize()
print data
p2 = deserialize(data)
print p2

print "-----------------"

registry = {}
def register_class(target_class):
    registry[target_class.__name__] = target_class

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

class Serializable_v3(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'class': self.__class__.__name__, 'args': self.args})

    @classmethod
    def deserialize(cls, data):
        params = json.loads(data)
        name = params['class']
        target_class = registry[name]
        return target_class(*params['args'])

class RegisteredSerializable(Serializable_v3):
    __metaclass__ = Meta

class Point2D(RegisteredSerializable):
    def __init__(self, x, y):
        super(Point2D, self).__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)

p1 = Point2D(2, 3)
print p1
data = p1.serialize()
print data
p2 = deserialize(data)
print p2