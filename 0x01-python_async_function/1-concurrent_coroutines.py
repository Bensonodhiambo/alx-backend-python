#!/usr/bin/env python3
"""Module for concurrently running n wait_random coroutines and returning the delays in ascending order."""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns the list of
    delays in ascending order.
    
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.
    
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    # Manual sorting by comparing as the results come in
    return sorted(delays)
