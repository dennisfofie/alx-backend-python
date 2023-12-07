#!/usr/bin/env python3
"""Defines the type annotated using function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Compute the multiplication of float"""

    def multiply(x: float) -> float:
        """Multiplying two numbers"""
        return x * multiplier

    return multiply
