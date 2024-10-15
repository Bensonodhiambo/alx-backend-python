#!/usr/bin/env python3
"""Module for measuring the runtime of wait_n coroutine."""

import time
import asyncio
from typing import List
from 1_concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns
    the average time per coroutine.
    
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.
    
    Returns:
        float: The average time taken per coroutine.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Execute the wait_n coroutine
    end_time = time.time()  # Record the end time

    total_time = end_time - start_time  # Calculate total execution time
    return total_time / n  # Return the average time per coroutine
