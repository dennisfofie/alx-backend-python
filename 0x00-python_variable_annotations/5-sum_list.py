#!/usr/bin/env python3
from typing import List

"""
Description - type-annotated function sum_list which takes a list input_list of floats as argument
"""


def sum_list(input_list: List[float]) -> float:
    """Returns sum of a list in float"""
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
