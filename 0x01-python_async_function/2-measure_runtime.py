#!/usr/bin/env python3
"""
this module creates a function to measure runtime
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ this function measures then returns runtime """
    tStamp1: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    tStamp2: float = time.time()
    total_time = tStamp2 - tStamp1
    return (total_time / n)
