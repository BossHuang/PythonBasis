__author__ = 'leihuang'

format_str = "hello, %s"
value = "H"
print format_str % value

format_str = "the score is %s - %s"
value = (2,1)
print format_str % value

from string import Template
s = Template("$x is $x.")
print s.substitute(x = "old")

s = Template("${x}est")
print s.substitute(x = "old")

s = Template("$name is $old")
people1 = {"name":"L","old":12}
print s.substitute(people1)

people2 = {"name":"H"}
print s.safe_substitute(people2)
# print s.substitute(people2)

pi = 3.14
print "%010.2f" % pi
print "%0*.*f" %(10,2,pi)

import string
print string.digits

s = "hello,world"
print s.find("l")
print s.find("l", 4)

s = ["1","2","3"]
flag = '+'
print flag.join(s)

dirs = '','usr','bin'
print '\\'.join(dirs)

s = "This's a book"
print s.lower()

import string
s = "this's a book"
print s.title()
print string.capwords(s)

s = "hello, world"
print s.replace('l', "T")

s = "hello, world"
print s.split(',')
print s.split()

s = "  ** hello, world **   "
print s
print s.strip()
print s.strip("*")

import string
table = string.maketrans("lo","ku")
s = "hello, world"
print s.translate(table)
print s.translate(table, ',')







