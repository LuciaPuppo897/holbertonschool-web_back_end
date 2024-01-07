#!/usr/bin/env python3
"""convert something into a async task using last task"""

import asyncio
from typing import List
task_wait_random = __import__('3-task').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Repets wait_n multiple times"""
    randomlist = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*randomlist)
    return sorted(delays)
