__author__ = 'leihuang'

a = [1,2,3,4]
first_two_number = a[:2]
print first_two_number
last_two_number = a[-2:]
print last_two_number

a = [1,2,3,4]
b = a[-0:]
print a
print b
print a is b

a = [1,2,3,4]
b = a[-2:]
print a, b
b[0] = 6
a[0] = 7
print a, b

a = [1,2,3,4]
a[1:3] = [6,7,8]
print a
