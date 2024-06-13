from decimal import Decimal

from typing import Callable

from calculator.operations import add, sub, mult, div

class calcOper:
    def __init__ (self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return calcOper(a, b, operation)

    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)

    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
