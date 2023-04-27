#!/usr/bin/env python3
from typing import List, Tuple, Sequence, Iterable

"""
Describe - function annotate a function to return list of tupel
"""


def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence], int]:
    return [(i, len(i)) for i in lst]
