#!/usr/bin/env python3
""" The basics of async module
"""


import asyncio
import random


async def wait_random(max_delay = 10):
    """ Wait random seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
