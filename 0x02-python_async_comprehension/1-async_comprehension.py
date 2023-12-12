#!/usr/bin/env python3
"""Coroutine that generate random numbers"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """generate random numbers using async generatar"""
    return [i async for i in async_generator()]
