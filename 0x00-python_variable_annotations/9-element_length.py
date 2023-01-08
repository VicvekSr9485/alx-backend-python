#!/usr/bin/env python3
""" ducking type an iterable object module
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return an annotated list
    """
    return [(i, len(i)) for i in lst]
