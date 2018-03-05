__author__ = 'leihuang'

#read mode
f = open("basicFileMethodsTestFile",'r')
print f.read()  #hello
f.close()

# write mode
f = open("basicFileMethodsTestFile",'w')
f.write("world")
f.close()

#read mode
f = open("basicFileMethodsTestFile",'r')
print f.read(2) #wo
print f.read() #rld
f.close()

f = open("basicFileMethodsTestFile",'w')
f.write("0123456789")
f.seek(3);
f.write("hello")
f.close()
f = open("basicFileMethodsTestFile",'r')
print f.read()
f.close()

f = open("basicFileMethodsTestFile",'r')
print f.read(2)
print f.tell()
f.close()