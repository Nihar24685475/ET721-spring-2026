"""
Nihar patel
March 3, 2026
lab 10, unit testing using pytest
"""

from calculator import *
import pytest

def test_add():
    assert add(2,3) == 5
    assert add(-8,5) == -3

def test_subtract():
    assert subtract(7,5) == 2
    assert subtract(-7,5) == -12 
    assert subtract(-7,-5) == -2


#lab exercise 1
def test_divide():
    assert divide(10,2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(3,0)

#lab exercise 2
def test_validate_password():
    assert validate_password("peter$pan") is True

def test_short_password():
    assert validate_password("pan") is False

def test_special_characters():
    assert validate_password("peter#pan") is False

#lab exercise 3 
@pytest.mark.parametrize(
    "n,expected",
    [
        (8, True),
        (-5, False),
        (0, True),
        (-12, True),
        (11, False)
    ]
)
def test_is_even(n, expected):
    assert is_even(n) == expected

#lab exercise 4 
#create a parametrizes test from

