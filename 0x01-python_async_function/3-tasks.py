#!/usr/bin/env python3
"""
this module creates a function that returns an asyncio.Task
"""
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ this function returns an asyncio.Task """
    task = asyncio.create_task(wait_random(max_delay))
    return task
