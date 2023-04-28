#!/usr/bin/env python3
"""advanced typing annotation using typevar"""
from typing import TypeVar, Mapping, Union, Any

K = TypeVar("K")  # Define a type variable for the key


def safely_get_value(
    dct: Mapping, key: Any, default: Union[K, None] = None
) -> Union[Any, K]:
    """More advanced typing"""
    if key in dct:
        return dct[key]
    else:
        return default
