import pytest
from decimal import Decimal
from calculator.calcOper import calcOper
from calculator.operations import add, sub, mult, div

def testOperation(a, b, operation, expected):
    calculation = calcOper.create(a, b, operation)
    assert calcOper.perform() == expected, f"{operation.__name__} operation has failed"

def testDivByZero():
    with pytest.raises(ValueError, match = "Error: Can't divide number by 0"):
        calculation = calcOper(Decimal('7'), Decimal('0'), div)
        calculation.perform()