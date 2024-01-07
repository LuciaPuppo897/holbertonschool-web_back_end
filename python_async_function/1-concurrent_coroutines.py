#!/usr/bin/env python3
"""Asynchronous coroutine that uses wait_random"""


import asyncio
from typing import List
import wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Asynchronous coroutine that spawns wait_random n times."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
