#!/usr/bin/env python3
"""
this module reuses previous module with updates to function calls
"""
import asyncio
from typing import List, Any
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ this function returns a list of all delays in ascending order """
    delayList: List[float] = []
    taskList: List[Any] = []
    for i in range(n):
        taskList.append(task_wait_random(max_delay))
    for results in asyncio.as_completed(taskList):
        firstRes = await results
        delayList.append(firstRes)
    return delayList
