"""
This module manages the history of various calculations
"""

from typing import List
from calculator_oper import CalculatorOper

class History:
    """
    This is a class with several methods to track history of calculations
    """
    _history: List[CalculatorOper] = []


    @classmethod
    def add_calculation(cls, calculation: CalculatorOper) -> None:
        """
        Adds a new calculation to the history.
        """
        cls._history.append(calculation)

    def get_last(self) -> CalculatorOper:
        """
        Retrieves the last calculation from history.
        If none, return empty
        """
        if not self._history:
            return None
        return self._history[-1]

    def get_all(self) -> List[CalculatorOper]:
        """
        Gets all calculations from the history
        """
        return self._history

    def __repr__(self):
        """
        Returns the string representation of the class.
        """
        return f"History({self._history})"
