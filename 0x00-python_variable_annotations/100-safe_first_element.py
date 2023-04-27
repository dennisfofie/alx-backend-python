#!/usr/bin/env python3
from typing import Sequence, Union, Any, NoneType

"""
Describe - variable annotation using the typing module to dynamically assigned
"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
