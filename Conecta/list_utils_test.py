import pytest
from list_utils import *

def test_find_one():
    needle = 1
    none = ['a',0,0,5,'s']
    beginning = [1, None, 9,5,4,3]
    ending = ['X', '0', 1]
    several = [0,0,3,4,1,4,2,1,4,5]

    assert find_one(none, needle) == False
    assert find_one(beginning, needle)
    assert find_one(ending, needle)
    assert find_one(several, needle)

def test_find_n():
    needle = 4
    n_beginning = [4,4,None,6,'a',7]
    n_ending = [5,6,7,4,4]
    n_middle = [1,2,3,4,4,5,6,7]
    more_than_n = [3,4,5,4,4,4,4,2,6]
    less_than_n = [1,2,3,4,5,6,7]
    none = [1,3,7,8,None]

    assert find_n(n_beginning, needle, 2)
    assert find_n(n_ending, needle, 2)
    assert find_n(n_middle, needle,2)
    assert find_n(more_than_n, needle, 3)
    assert find_n(less_than_n, needle, 2) == False
    assert find_n(none, needle, 2) == False
    assert find_n(n_beginning, needle, 0) == False
    assert find_n(n_beginning, needle, -10) == False

def test_find_streak():
    needle = 1
    none = ['a',0,0,5,'s']
    beginning = [1,1,1,9,5,4,3]
    ending = ['X','0',1,1,1]
    more_than_n = [0,0,3,1,1,1,1,None]
    no_streak = [1,3,1,4,3,1,1,]

    assert find_streak(none, needle, 1) == False
    assert find_streak(beginning, needle, 3)
    assert find_streak(ending, needle, 3)
    assert find_streak(more_than_n, needle, 3)
    assert find_streak(no_streak, needle, 4) == False
    assert find_streak(none, needle, 0) == False
    assert find_streak(none, needle, -10) == False