__author__ = 'leihuang'

class Exam(object):
    def __init__(self):
        self._write_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <=100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def write_grade(self):
        return self._write_grade

    @write_grade.setter
    def write_grade(self, value):
        self._check_grade(value)
        self._write_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @ math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value

class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <=100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value

class Exam_with_descriptor(object):
    write_grade = Grade()
    math_grade = Grade()

e = Exam_with_descriptor()
e.math_grade = 5
print e.math_grade
e.write_grade = 3
print e.write_grade

a = Exam_with_descriptor()
a.math_grade = 5
b = Exam_with_descriptor()
b.math_grade = 10
print a.math_grade
print b.math_grade
Exam_with_descriptor.math_grade = 7
print a.math_grade
print b.math_grade

from weakref import WeakKeyDictionary
class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <=100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

a = Exam_with_descriptor()
a.math_grade = 5
b = Exam_with_descriptor()
b.math_grade = 10
print a.math_grade
print b.math_grade
Exam_with_descriptor.math_grade = 7
print a.math_grade
print b.math_grade
