#!/usr/bin/env python3
"""
this module writes a coroutine and imports a second coroutine
"""
from typing import List, Any
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Any]:
    """ this coroutine comprehenses over imported coroutine """
    randos = [i async for i in async_generator()]
    return randos
