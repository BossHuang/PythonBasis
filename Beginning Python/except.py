__author__ = 'leihuang'

import exceptions
print dir(exceptions)

class SomeCustomException(Exception):
    pass

def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print "y can not be 0"
    except TypeError:
        print "x or y is not a number"

print division(1.0, 0.0)

def division(x,y):
    try:
        return x/y
    except:
        print "x or y is wrong"

def division(x,y):
    try:
        return x/y
    except Exception, e:
        print e
division(1,0)

def division(x,y):
    try:
        print x/y
        #return x/y
    except:
        print "except"
    else:
        print "else"
    finally:
        print "finally"

division(1,0)
division(1,2.0)

def division(x,y):
    try:
        return x/y
    except:
        if y == 0:
            print "y can not be zero"
        else:
            raise

division(1,0)
division('1',2)