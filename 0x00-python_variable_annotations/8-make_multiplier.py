#!/usr/bin/env python3
""" Complex types - functions module
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function multiplier
    """
    return lambda x: multiplier * x
