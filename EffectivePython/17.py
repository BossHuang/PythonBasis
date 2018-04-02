__author__ = 'leihuang'

def get_value():
    values = [5.0,6.0,7.0]
    for x in values:
        yield x

def normalize(numbers):
    total = sum(numbers)
    result = []
    for x in numbers:
        result.append(x/total)
    return result

print normalize(get_value())

#----------------------

def get_value():
    values = [5.0,6.0,7.0]
    for x in values:
        yield x

def normalize(get_iter):
    total = sum(get_iter())
    result = []
    for x in get_iter():
        result.append(x/total)
    return result

print normalize(lambda: get_value())

#-------------------

class ReadValue():
    def __init__(self, values):
        self.valus = values
    def __iter__(self):
        for value in self.valus:
            yield value

def normalize(numbers):
    total = sum(numbers)
    result = []
    for x in numbers:
        result.append(x/total)
    return result

values = ReadValue([5.0,6.0,7.0])
print normalize(values)

#---------------
def normalize(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must suply a container')
    total = sum(numbers)
    result = []
    for x in numbers:
        result.append(x/total)
    return result

values = [5.0,6.0,7.0]
print normalize(values)
