__author__ = 'leihuang'

class ToDictMixIn(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixIn):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class BinaryTree(ToDictMixIn):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)), right=BinaryTree(13, left=BinaryTree(11)))
print tree.to_dict()
print tree.__dict__
print BinaryTree.__dict__

class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super(BinaryTreeWithParent, self).__init__(value, right=right, left=left)
        self.parent = parent
    def _traverse(self, key, value):
        if isinstance(value, BinaryTreeWithParent) and key == 'parent':
            return value.value
        else:
            return super(BinaryTreeWithParent, self)._traverse(key, value)

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.right = BinaryTreeWithParent(9, parent=root)
print root.to_dict()

import json
class JsonMixIn(object):
    @classmethod
    def from_json(cls, data):
        kwargs = json.load(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())

class DatacenterRack(ToDictMixIn, JsonMixIn):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [Machine(**kwargs) for kwargs in machines]

class Switch(ToDictMixIn, JsonMixIn):
    pass

class Machine(ToDictMixIn, JsonMixIn):
    pass