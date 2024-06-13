"""
This is a module that has 4 basic arithmetic functions such as
addition, subtraction multiplication, and division
"""

from decimal import Decimal

def add(num1: Decimal, num2: Decimal) -> Decimal:
    """
    Returns the value of two decimals added
    """
    return num1 + num2

def sub(num1: Decimal, num2: Decimal) -> Decimal:
    """
    Returns the value of two decimals subtracted
    """
    return num1 - num2

def mult(num1: Decimal, num2: Decimal) -> Decimal:
    """
    Returns the value of two decimals multiplied
    """
    return num1 * num2

def div(num1: Decimal, num2: Decimal) -> Decimal:
    """
    Returns the value of two decimals divided
    """
    if num2 == 0:
        raise ValueError("Error: Can't divide number by 0")
    return num1 / num2
