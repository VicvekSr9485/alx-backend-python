#!/usr/bin/env python3
""" Asyncio Tasks module
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """ return asyncio.Tasks
    """
    return asyncio.Task(wait_random(max_delay))
