import pytest
from linear_board import *
from setting import *

def test_empty_board():
    empty = LinearBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory('x') == False

def test_add():
    b = LinearBoard()
    for i in range(BOARD_COLUMN_SIZE):
        b.add('x')
    assert b.is_full() == True

def test_victory():
    pass

def test_tie():
    b = LinearBoard()

    b.add('o')
    b.add('o')
    b.add('x')
    b.add('o')

    assert b.is_tie('x','o')