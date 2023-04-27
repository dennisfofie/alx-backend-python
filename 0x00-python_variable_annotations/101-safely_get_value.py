#!/usr/bin/env python3
from typing import TypeVar, Optional, Dict

"""
Description - is a generic type that allows you to define a type variable that can be used in place of an actual type.
"""


K = TypeVar("K")  # Define a type variable for the key
V = TypeVar("V")  # Define a type variable for the value


def safely_get_value(
    dct: Dict[K, V], key: K, default: Optional[V] = None
) -> Optional[V]:
    if key in dct:
        return dct[key]
    else:
        return default
