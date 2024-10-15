#!/usr/bin/env python3
"""Module for an asynchronous coroutine that waits for a random delay"""

import asyncio
import random
from typing import Coroutine


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    (included as a float) seconds and returns the actual delay.
    
    Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.
    
    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
