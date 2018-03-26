__author__ = 'leihuang'

a = ['a','bc','cde']
it = (len(x) for x in a)
print it
print next(it)

y = ((x, x**2) for x in it)
print y
print list(y)