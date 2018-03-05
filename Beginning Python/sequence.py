__author__ = 'leihuang'

# sequence has sequence
A = [1, "a"]
B = [2, "b"]
C = [A, B]
print C

print ""
# indexing
print "hello world"[0]
print "hello world"[-1]

#number = raw_input("year:")[0]
#print number

number = [1,2,3,4,5,6,7,8,9,10]

# get last 3 numbers
print number[-3:]

# get before 3 numbers
print number[:3]

# copy all sequence
print number[:]

# step length is 2
print number[0:5:2]
print number[::2]

# step length is -2
print number[::-2]

print [1,2,3]+[4,5,6]
print "Hello "+"world"

print "Python"*2
print [1,2]*2
print [None]*2

print 1 in number
print 0 in number

print len(number)
print max(number)
print min(number)
print max(1,2,3)
print min(1,2,3)