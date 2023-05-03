#!/usr/bin/env python3
"""Coroutine that generate random numbers"""
import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> list[float]:
    """generate random numbers using async generatar"""
    return [i async for i in async_generator()]
