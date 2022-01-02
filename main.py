from Calculator import *
import pytest

def test_add_two_small_numbers():
    calc = Calculator()
    actual = calc.add(3, 4)
    expected = 7
    assert actual == expected

# (venv) D:\python_projects\today_02Jan22\02.01.2022>pytest main.py