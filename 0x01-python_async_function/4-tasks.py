#!/usr/bin/env python3
"""Module for concurrently running n task_wait_random coroutines and returning the delays in ascending order."""

import asyncio
from typing import List
from 3_tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns the list
    of delays in ascending order.
    
    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for each task_wait_random call.
    
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Wait for all tasks to complete and gather the results
    delays = await asyncio.gather(*tasks)

    # Return the delays sorted in ascending order
    return sorted(delays)
