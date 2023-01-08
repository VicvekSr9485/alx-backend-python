#!/usr/bin/env python3
""" Complex types - string and int/float to tuple module
"""

from typing import List, Union, Tuple

def to_kv(k: str, v: Union[int, float])  -> Tuple[str, float]:
    """ returns a tuple of string and float
    """
    return (k, v**2)
