#!/usr/bin/env python3
"""Coroutine that measure runtime of async comprehension"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measure runtime of async coroutine"""
    start_time = time.perf_counter()
    results = [async_comprehension() for i in range(4)]
    await asyncio.gather(*results)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time
