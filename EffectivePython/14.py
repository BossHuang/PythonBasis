__author__ = 'leihuang'

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

print divide(1.0,0)
print divide(0, 2)


def divide(a, b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError, e:
        raise ValueError('Invalid input')

print divide(1,0)