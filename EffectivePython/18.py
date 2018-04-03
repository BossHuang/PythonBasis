__author__ = 'leihuang'

def log(message, values):
    if not values:
        print message
    else:
        values_str = ', '.join(str(x) for x in values)
        print "%s: %s" %(message, values_str)

log("My phone is ", [1,2,3])
log("Hi",[])

def log(message, *values):
    if not values:
        print message
    else:
        values_str = ', '.join(str(x) for x in values)
        print "%s: %s" %(message, values_str)

log("My phone is ", [1,2,3])
log("Hi")

def log(message, *values):
    if not values:
        print message
    else:
        values_str = ', '.join(str(x) for x in values)
        print "%s: %s" %(message, values_str)

log("My phone is ", *[1,2,3])