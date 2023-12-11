#!/usr/bin/env python3
"""Computes the sort of a list"""


def sort_list(n: list[int | float]) -> list:
    """Sort list in asc order"""
    for i in range(len(n)):
        for j in range((len(n) - 1)):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n
