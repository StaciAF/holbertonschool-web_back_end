#!/usr/bin/env python3
"""
this module writes an async coroutine with random delay
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ this coroutine waits for a random delay then returns the delay time """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
