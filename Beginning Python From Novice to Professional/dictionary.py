__author__ = 'leihuang'

items = [('name','L'),('age',10)]
d = dict(items)
print d

items = [['name','L'],['age',10]]
d = dict(items)
print d

d = dict(name = 'L', age = 10)
print d

d = dict()
print d

c = {'age': 10, 'name': 'L'}
d = dict(c)
print c
print d
d['age'] = 11
print d
print c

d = {'age': 10, 'name': 'L'}
print "L is %(age)s" % d

d = {'age': 10, 'name': 'L'}
c = d.clear()
print d
print c

x = {}
y = x
x['key'] = 'value'
print x
print y
y = {}
print x
print y

x = {}
y = x
x['key'] = 'value'
print x
print y
x.clear()
print x
print y

d = {'age': 10, 'name': ['L','M']}
c = d.copy()
print d
print c
c['age'] = 11
c['name'].remove('M')
print d
print c

import copy
d = {'age': 10, 'name': ['L','M']}
c = copy.deepcopy(d)
c['age'] = 11
c['name'].remove('M')
print d
print c

keys = ['name','age']
print {}.fromkeys(keys)
print dict.fromkeys(keys)
print dict.fromkeys(keys, False)

x = {}
print x.get('name')
print x.get('name','L')

x = {'name':'L'}
print x.has_key('name')
print x.has_key('age')

d = {'age': 10, 'name': ['L','M']}
print d.items()
it = d.iteritems()
print it
print list(it)

d = {'age': 10, 'name': ['L','M']}
print d.keys()
it = d.iterkeys()
print it
print list(it)

d = {'age': 10, 'name': ['L','M']}
c = d.pop('name')
print c
print d

d = {'age': 10, 'name': ['L','M']}
print d.popitem()
print d

d = {}
print d.setdefault('name')
print d
print d.setdefault('name','L')
print d

d = {'age': 10, 'name': 'L'}
c = {'age': 11, 'address':'M'}
d.update(c)
print d
print c

d = {'age': 10, 'name': 'L'}
print d.values()
it = d.itervalues()
print it
print list(it)