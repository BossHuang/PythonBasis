__author__ = 'leihuang'


def palindrome(word):
    """
    Return True if the given word is a palindrome.
    """
    return word == word[::-1]

print palindrome.__doc__

print "===================="

import time
print time.__doc__

print "===================="

from threading import Thread
print Thread.__doc__

class Player(object):
    """Repressents a plater of the game

    Subclasses may override the 'tick' method to provide
    custom animations for the player's movement depending
    on theri power level, etc.

    Public attributes:
    - power: Unused power-ups (float between 0 and 1)
    - coins: Coins found during the level (integer)

    """
    pass

print "===================="

import math
print math.acos.__doc__

def find_anagrams(word, dictionary):
    """ Find all anagrams for a word.

    This function only runs as fast as the test for
    membership in the 'dictionary' container. It will
    be slow if the dictionary is a list and fast if
    it's a set

    :param word: String of the target word
    :param dictionary: Container with all strings that
                are known to be actual words.
    :return: List of anagrams that were found. Empty if none were found.
    """