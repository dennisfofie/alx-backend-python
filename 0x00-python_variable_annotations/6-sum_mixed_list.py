#!/usr/bin/env python3
"""
Description - return sum of all the elements in a list by checking the type
"""


def sum_mixed_list(mxd_lst: list[int, float]) -> float:
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
