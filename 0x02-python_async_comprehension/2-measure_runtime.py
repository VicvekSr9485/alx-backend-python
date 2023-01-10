#!/usr/bin/env python3
""" Run time for four parallel comprehensions module
"""

import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the total runtime of four parallel coroutines
    """
    
