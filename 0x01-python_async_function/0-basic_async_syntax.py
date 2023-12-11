#!/usr/bin/env python3
"""async coroutine that wait for result"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Compute random of a int"""
    result: float = uniform(0, max_delay)
    await asyncio.sleep(result)
    return result
