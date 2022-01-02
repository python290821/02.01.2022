from Calculator import *
import pytest

def test_add_two_small_numbers():
    calc = Calculator()
    actual = calc.add(3, 4)
    expected = 7
    assert [3,4] == [3,4, 5]
