#!/usr/bin/env python3
"""Defines list typing usin tuple"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Compute tuple of a sequence and int"""
    return [(i, len(i)) for i in lst]
