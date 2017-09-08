__author__ = 'leihuang'

str = "Hello World"
# str[0] = 'F'    # error

# transform str to list
str_to_list = list(str)
print str_to_list

# transform list to str
list_to_str = ''.join(str_to_list)
print list_to_str

a = [1,2,3]
a[1] = 4
print a

a = [1,2,3]
del a[1]
print a

a = [1,2,3]

a[1:] = [9,8]
print a

a[1:1] = [6,5]
print a

a[1:3] = []
print a

a = [1,2]
a.append(3)
print a

a = [1,2,3,1]
print a.count(1)

a = [1,2]
b = [3,4]
a.extend(b)
print a

print a+b
print a

a = [1,2,1,2]
print a.index(2)

a = [1,3]
a.insert(1, 2)
print a

a = [1,2,3,4,5]
print a.pop()
print a

print a.pop(1)
print a

a = [1,2,1,2]
a.remove(2)
print a

a = [1,2,3]
a.reverse()
print a

a = [1,3,2]
a.sort()
print a

a = [1,3,2]
b = a[:]
b.sort()
print a
print b

c = sorted(a)
print c
print a

a = ["h","hel","he"]
a.sort(key = len)
print a

a = ["h","hel","he"]
a.sort(key=len, reverse=True)
print a