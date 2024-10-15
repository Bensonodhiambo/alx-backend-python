#!/usr/bin/env python3
"""Module to create an asyncio Task for wait_random."""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
