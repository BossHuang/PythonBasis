__author__ = 'leihuang'

class FrequencyList(list):
    def __init__(self, numbers):
        super(FrequencyList, self).__init__(numbers)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts

f = FrequencyList([1,2,1,3,4,2,2])
print f.frequency()
print len(f)

class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class ListBinaryNode(BinaryNode):
    def _count(self, node):
        count = 0
        if node.value!=None:
            count += 1
        if node.left:
            count += node._count(node.left)
        if node.right:
            count +=  node._count(node.right)
        return count

    def __len__(self):
        return self._count(self)


a = ListBinaryNode(5, left=ListBinaryNode(3, left=ListBinaryNode(1)), right=ListBinaryNode(2,right=ListBinaryNode(3)))
print len(a)


from collections import Sequence

class Test(Sequence):
    print "Test"

t = Test()

