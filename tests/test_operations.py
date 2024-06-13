"""This is a test file that has two functions, the first is to test different operations and ensure
   that the they work, otherwise, a error message is thrown saying that the operation has failed. 
   The 2nd function is to a test that has a number divided by 0, and throws a error saying you can't
   divide by 0."""

import pytest
from decimal import Decimal
from calculator.calcOper import calcOper
from calculator.operations import add, sub, mult, div


def test_Op(a: Decimal, b: Decimal, operation, expected):
    calculation = calcOper.create(a, b, operation)
    assert calcOper.perform() == expected, f"{operation.__name__} operation has failed"
    '''Tests that operations work, otherwise the operation has failed.'''


def test_Div_Zero():
    with pytest.raises(ValueError, match = "Error: Can't divide number by 0"):
        calculation = calcOper(Decimal('7'), Decimal('0'), div)
        calculation.perform()
        '''Is a test to throw an error if a number is divided by zero, if zero then throw error'''
