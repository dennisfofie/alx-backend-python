#!/usr/bin/env python3
from typing import Union, Tuple

"""
Description- type-annotated function that takes string
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (
        k,
        v**2,
    )
