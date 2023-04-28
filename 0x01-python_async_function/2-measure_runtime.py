#!/usr/bin/env python3
"""Measure the time for execution"""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Average time the function took in execution"""
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.perf_counter()
    total_time: float = end_time - start_time
    return total_time / n
