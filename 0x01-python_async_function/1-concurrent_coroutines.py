#!/usr/bin/env python3
"""
this module writes an async routine using wait_random coroutine
"""
import asyncio
from typing import List, Any
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ this function returns a list of all delays in ascending order """
    delayList: List[float] = []
    taskList: List[Any] = []
    for i in range(n):
        taskList.append(asyncio.create_task(wait_random(max_delay)))
    for results in asyncio.as_completed(taskList):
        firstRes = await results
        delayList.append(firstRes)
    return delayList
