#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay (inclusive).

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay that was waited for.
    """
    delay = random.uniform(0, max_delay)  # Generate a random float delay
    await asyncio.sleep(delay)  # Wait for the generated delay
    return delay  # Return the delay value
