#!/usr/bin/env python3
"""Measures the average execution time for wait_n(n, max_delay)."""


import asyncio
import time
from typing import List
from concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the average execution time for wait_n(n, max_delay)."""
    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
