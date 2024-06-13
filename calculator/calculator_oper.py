"""
This is a module that used to handle math operations with between two operands
"""

from decimal import Decimal

from typing import Callable

class CalculatorOper:
    """
    As previously stated before this class is used to handle operations between two operands.
    """
    def __init__ (self, num1: Decimal, num2: Decimal,
                  operation: Callable[[Decimal, Decimal], Decimal]):
        """Constructor to initialize a CalculatorOper instance with two operands and one operator"""
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    @staticmethod
    def create(num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Factory method as a different way to initialize a new CalculatorOper class object.
        """
        return CalculatorOper(num1, num2, operation)

    def perform(self) -> Decimal:
        """
        This method performs the operation between the two operands
        that is stored inside the class instance.

        """
        return self.operation(self.num1, self.num2)

    def __repr__(self):
        """
        This method returns the string representation of the class instance
        """
        return f"Calculation({self.num1}, {self.num2}, {self.operation.__name__})"
