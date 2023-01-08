#!/usr/bin/env python3
""" Duck typing - first element of a sequence module
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns a complex annotated list """
    if lst:
        return lst[0]
    else:
        return None
