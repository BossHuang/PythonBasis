__author__ = 'leihuang'

##############################
# NumbersandExpressions
#   /
print "/"
print 1/2       #0
print 1.0/2     #0.5
print 1/2.      #0.5

print ""
#   //
print "//"
print 1//2.0    #0.0
print 1.0//2.0  #0.0
print 1//2      #0

print ""
#   %
print "%"
print 10%3      #1
print 2.75%0.5  #0.25

print ""
#   **
print "**"
print 3**2      #9
print -3**2     #-9
print 3**-2     #0.1111
print (-3)**2   #9

print ""
# Hexadecimals
print "Hexadecimals"
print 0xAF      #175
# Octals
print "Octals"
print 010       #8
##############################
print
print
##############################
#  get user input
print "input"
x = input("x:")
y = input("y:")
print x*y

name = input("What is your name?")
print "Hi "+name

print
print "raw_input"
x = raw_input("x:")
y = raw_input("y:")
print float(x)*float(y)

name = raw_input("What is your name?")
print "Hi "+name

print type(raw_input("please input:"))

##############################
print
print
#############################

# import
import math
print math.sqrt(9)

func = math.sqrt
print func(9)

from cmath import sqrt
from math import sqrt
print sqrt(9)

##############################
print
print
#############################
# ''  ""

print "Let's go"
print '"Hello World", I said'

print "hello "+str(100)
print "heool "+`100`
print "heool "+repr(100)