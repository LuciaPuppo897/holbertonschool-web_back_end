#!/usr/bin/env python3
"""Asynchronous coroutine that waits for a random delay"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """oroutine that waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay) # is not espcecified
    return delay
