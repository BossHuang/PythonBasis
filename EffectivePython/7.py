__author__ = 'leihuang'

a = [1,2,3,4,5]
result = map(lambda x:x**2, filter(lambda x:x%2==0, a))
print result
result = [x**2 for x in a if x%2==0]
print result

x = {1:'a',2:'b'}
y = {value:key for key,value in x.items()}
print y

x = {'a','bc','cde'}
y = {len(v) for v in x}
print y
