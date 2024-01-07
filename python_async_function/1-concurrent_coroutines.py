#!/usr/bin/env python3
"""Asynchronous coroutine that uses wait_random"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that spawns wait_random n times."""
    randomlist = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*randomlist)
    return sorted(delays)
