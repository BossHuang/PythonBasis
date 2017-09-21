__author__ = 'leihuang'

# print "---"
# import Hi
# print "---"
# import Hi
# print "---"
# Hi = reload(Hi)
# print "---"
#
# import Hi2
# Hi2.Hello()
#
# from HelloWrold import Hello
# import HelloWrold.World
#
# import copy
# print [n for n in dir(copy) if not n.startswith('_')]
# print copy.__all__
#
# print copy.copy.__doc__
# help(copy.copy)

# print range.__doc__
#
# import copy
# print copy.__file__

a = set([1,2,3,4])
b = set([2,3,4,5])
print a.union(b)
print a | b

print a.intersection(b)
print a & b

print a.difference(b)
print a - b

print a.symmetric_difference(b)
print a ^ b

c = a & b
print c.issubset(a)
print c.issuperset(a)
print a.copy() is a
print a.copy() == a

a = set([1,2])
b = set([2,3])
a.add(frozenset(b))
print a




