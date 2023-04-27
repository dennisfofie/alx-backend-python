#!/usr/bin/env python3
from typing import Optional, Dict, TypeVar

"""
Description - Use mypy to validate the following piece of code and apply any necessary changes.
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
