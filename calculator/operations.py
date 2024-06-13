from decimal import Decimal


def add(a: Decimal, b: Decimal) -> Decimal: #(Type hints are to ensure that a and b are decimal values and -> Decimal hints that a decimal is returned)
    return a + b

def sub(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def mult(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def div(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Error: Can't divide number by 0")
    return a / b
