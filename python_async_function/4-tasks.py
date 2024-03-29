#!/usr/bin/env python3
"""convert something into a async task using last task"""


from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Repets wait_n multiple times"""
    randomlist = []
    for _ in range(n):
        randomlist.append(await task_wait_random(max_delay))
    return sorted(randomlist)
