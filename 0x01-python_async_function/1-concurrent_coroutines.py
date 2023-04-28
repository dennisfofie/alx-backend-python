#!/usr/bin/env python3
"""Describe a file that returns function"""
from sort import sort_list

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Sort a list of float in ascending order"""
    results: list = []
    for _ in range(n):
        result: float = await wait_random(max_delay)
        results.append(result)
    return sort_list(results)
