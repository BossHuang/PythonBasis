__author__ = 'leihuang'

a = [[1,2,3],[4,5,6]]
b = [x for row in a for x in row]
print b

squared = [[x**2 for x in row] for row in a]
print squared
