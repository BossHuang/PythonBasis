__author__ = 'leihuang'

names = ['Socrates','Archimedes','Plato']
names.sort(key=lambda x:len(x))
print names

from collections import defaultdict
def log_missing():
    print 'Key add'
    return 0

current = {'green':12,'blue':3}
increment = [('red',2),('blue',3),('orange',4)]
result = defaultdict(log_missing, current)
print result
print 'before:',(result)
for key,value in increment:
    result[key] += value
print 'after:',dict(result)

def increment_with_current(current, increment):
    added_count = [0]

    def missing():
        added_count[0] += 1
        return 0

    result = defaultdict(missing, current)
    for key, value in increment:
        result[key] += value

    return result, added_count[0]

current = {'green':12,'blue':3}
increment = [('red',2),('blue',3),('orange',4)]
result, added_count = increment_with_current(current, increment)
print dict(result), added_count

class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

current = {'green':12,'blue':3}
increment = [('red',2),('blue',3),('orange',4)]
counter = CountMissing()
result = defaultdict(counter.missing, current)
for k,v in increment:
    result[k] += v
print counter.added

class BetterCounterMissing(object):
    def __init__(self):
        self.added = 0
    def __call__(self):
        self.added += 1
        return 0
counter = BetterCounterMissing()
print callable(counter)
current = {'green':12,'blue':3}
increment = [('red',2),('blue',3),('orange',4)]
result = defaultdict(counter, current)
for k,v in increment:
    result[k] += v
print counter.added