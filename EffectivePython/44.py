__author__ = 'leihuang'

class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4

state = GameState()
state.level += 2
state.lives -= 3
print state.__dict__

import pickle
state_path = './game_state.pickle'
with open(state_path, 'wb') as f:
    pickle.dump(state, f)

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)

print state_after.__dict__

print "====================="

class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.point = 0

import pickle
state_path = './game_state.pickle'
with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print state_after.__dict__

print "====================="

class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4

def pickle_obj(obj):
    kwargs = obj.__dict__
    return unpickle_obj, (kwargs,)

def unpickle_obj(kwargs):
    return GameState(**kwargs)

import copy_reg
copy_reg.pickle(GameState, pickle_obj)

state = GameState()
state.level += 2
state.lives -= 3
print state.__dict__

import pickle
state_path = './game_state_v2.pickle'

with open(state_path, 'wb') as f:
    pickle.dump(state, f)

class GameState(object):
    def __init__(self, level=0, lives=4, point=0):
        self.level = level
        self.lives = lives
        self.point = point

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print state_after.__dict__

print "====================="

class GameState(object):
    def __init__(self, level):
        self.level = level

def pickle_obj(obj):
    kwargs = obj.__dict__
    kwargs['version'] = 2
    return unpickle_obj, (kwargs,)

def unpickle_obj(kwargs):
    version = kwargs.pop('version', 1)
    if version == 1:
        kwargs.pop('lives')
    return GameState(**kwargs)

import copy_reg
copy_reg.pickle(GameState, pickle_obj)

import pickle
state_path = './game_state_v2.pickle'

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print state_after.__dict__

print "====================="

class GameStateSecond(object):
    def __init__(self, level=0, lives=4):
        self.level = level
        self.lives = lives

def pickle_obj(obj):
    kwargs = obj.__dict__
    return unpickle_obj, (kwargs,)

def unpickle_obj(kwargs):
    return GameStateSecond(**kwargs)

import copy_reg
copy_reg.pickle(GameStateSecond, pickle_obj)

import pickle
state_path = './game_state_v2.pickle'

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print state_after.__dict__
