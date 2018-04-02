__author__ = 'leihuang'

def sort_prior(values, group):
    print "out begin"
    def helper(x):
        print x,"in"
        if x in group:
            return (0, x)
        return (1, x)
    print "out end"
    values.sort(key=helper)
    print "out end2"

values = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sort_prior(values, group)
print values

#-------------------------------------

def sort_prior_v2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

values = [8,3,1,2]
group = {2,3}
result = sort_prior_v2(values, group)
print result, values

#-------------------------------------

def sort_prior_python2(values, group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found[0]

values = [8,3,1,2]
group = {2,3}
result = sort_prior_python2(values, group)
print result, values

#-------------------------------------

class Sorter():
    def __init__(self, group):
        self.found = False
        self.group = group
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1,x)

values = [8,3,1,2]
group = {2,3}
sorter = Sorter(group)
values.sort(key=sorter)
print values
print sorter.found