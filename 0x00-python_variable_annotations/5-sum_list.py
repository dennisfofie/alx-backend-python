#!/usr/bin/env python3
"""Define sum of a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes list of float element sum of a list in float"""
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
