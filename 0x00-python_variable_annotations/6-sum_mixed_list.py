#!/usr/bin/env python3
""" Complex types - mixed list module
"""

from typing import List, Union


def sum_mixed_list(mxd_lst:  List[Union[int, float]]) -> float:
    """ return the sum of mxd_lst
    """
    return sum(mxd_lst)
