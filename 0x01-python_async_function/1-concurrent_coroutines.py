#!/usr/bin/env python3
"""Describe a file that returns function"""
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Sort a list of float in ascending order"""
    results: list = []
    for _ in range(n):
        result: float = await wait_random(max_delay)
        results.append(result)
    return sorted(results)
