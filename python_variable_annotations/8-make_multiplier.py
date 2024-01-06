#!/usr/bin/env python3
"""Returns a function that multiplies a float by multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """define a function"""
    def multiplier_function(x: float) -> float:
        """define another function"""
        return x * multiplier

    return multiplier_function
