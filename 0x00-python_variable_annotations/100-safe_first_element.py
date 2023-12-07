#!/usr/bin/env python3
"""duck type function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The duck type using sequence"""
    if lst:
        return lst[0]
    else:
        return None
