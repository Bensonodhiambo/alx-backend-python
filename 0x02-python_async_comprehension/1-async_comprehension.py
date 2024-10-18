#!/usr/bin/env python3
"""
This module contains the coroutine async_comprehension that collects 10 random
numbers from the async_generator.
"""

from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator and returns the list of random numbers.
    """
    return [num async for num in async_generator()]
