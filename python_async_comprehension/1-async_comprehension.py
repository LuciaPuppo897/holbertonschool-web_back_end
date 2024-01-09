#!/usr/bin/env python3
"""calls async_generator and do the same but with args"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous coroutine that collects 10 random numbers using async"""
    result = [num async for num in async_generator()]
    return result
