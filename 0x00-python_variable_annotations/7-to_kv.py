#!/usr/bin/env python3
"""Define tuple of string and float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Compute the tuple of str and float"""
    return (
        k,
        v**2,
    )
