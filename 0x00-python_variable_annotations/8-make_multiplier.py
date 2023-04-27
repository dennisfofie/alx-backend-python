#!/usr/bin/env python3
from typing import Callable

"""
Describe - type-annotated function that takes a float and returns multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
