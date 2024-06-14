"""
This is a module to test the operators from operators.py
"""

from decimal import Decimal
import pytest
from calculator.operations import add, sub, mult, div

def test_addition():
    """
    Test if addition works properly
    """
    assert add(3, 4) == Decimal(7)

def test_subtraction():
    """
    Test if subtraction works properly
    """
    assert sub(5, 2) == Decimal(3)

def test_multiplication():
    """
    Test if multiplication works properly
    """
    assert mult(2, 3) == Decimal(6)

def test_division():
    """
    Test if division works properly
    """
    assert div(10, 2) == Decimal(5)

def test_division_by_zero():
    """
    Test if divide by zero raises value error
    """
    with pytest.raises(ValueError):
        div(5, 0)

def test_float_addition():
    """
    Test that floating addition works
    """
    result = round(add(0.1, 0.2), 1)
    assert Decimal(str(result)) == Decimal("0.3")


def test_negative_subtraction():
    """
    Test if negative subtraction works properly
    """
    assert sub(-5, -2) == Decimal(-3)
