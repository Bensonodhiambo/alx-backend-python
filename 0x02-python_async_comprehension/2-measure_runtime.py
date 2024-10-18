#!/usr/bin/env python3
"""
This module contains the coroutine measure_runtime that executes
async_comprehension four times in parallel and measures the runtime.
"""

import asyncio
import time
from async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel using asyncio.gather.
    
    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()  # Start measuring time
    # Run four instances of async_comprehension in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()  # End measuring time
    
    return end_time - start_time  # Return the total runtime
