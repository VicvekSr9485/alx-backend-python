#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async
"""

wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List
import random
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ returns multiple coroutines
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
