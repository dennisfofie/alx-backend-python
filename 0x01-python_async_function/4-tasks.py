#!/usr/bin/env python3
"""Describe a file that returns function"""

task_wait_random = __import__("3-tasks").wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Sort a list of float in ascending order"""
    results: list = []
    for _ in range(n):
        result: float = await task_wait_random(max_delay)
        results.append(result)
    return sorted(results)
