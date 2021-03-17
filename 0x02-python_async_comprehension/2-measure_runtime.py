#!/usr/bin/env python3
"""
this module creates a function to measure runtime of parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ this coroutine measures runtime then returns it """
    timeStamp1: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),       async_comprehension()
    )
    timeStamp2: float = time.time()
    lapsed: float = timeStamp2 - timeStamp1
    return lapsed
