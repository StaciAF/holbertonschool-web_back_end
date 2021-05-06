#!/usr/bin/env python3
"""
this module writes a coroutine
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ this coroutine yields a random float between 0 and 10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
