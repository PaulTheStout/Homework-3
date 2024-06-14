"""
Basic arithmetic calculator module
"""

from typing import Callable
from decimal import Decimal
from calculator_oper import CalculatorOper
from history import History
import operations

class Calculator:
    """
    A class to perform basic arithmetic calculations.
    """

    def __init__(self):
        self._history = History()

    @staticmethod
    def _perform_operation(
        num1: Decimal, num2: Decimal,
        operation: Callable[[Decimal, Decimal], Decimal],
        history: History
    ):
        """
        Perform the specified operation.
        
        Static method as it operates on input numbers and 
        operation independently of instance-specific data.
        """

        calculation = CalculatorOper.create(num1, num2, operation)
        result = calculation.perform()
        history.add_calculation(calculation)
        return result

    def add(self, num1: Decimal, num2: Decimal) -> Decimal:
        """
        Perform addition
        """
        return self._perform_operation(num1, num2, operations.add, self._history)

    def sub(self, num1: Decimal, num2: Decimal) -> Decimal:
        """
        Perform subtraction
        """
        return self._perform_operation(num1, num2, operations.sub, self._history)

    def mult(self, num1: Decimal, num2: Decimal) -> Decimal:
        """
        Perform multiplication
        """
        return self._perform_operation(num1, num2, operations.mult, self._history)

    def div(self, num1: Decimal, num2: Decimal) -> Decimal:
        """
        Perform division
        """
        return self._perform_operation(num1, num2, operations.div, self._history)
