#!/usr/bin/env python3
"""coroutine that asynchronously loop 10 times"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """This generate random numbers while sleeping 1sec"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
