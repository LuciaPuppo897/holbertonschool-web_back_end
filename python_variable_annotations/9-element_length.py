#!/usr/bin/env python3
"""Returns a list of tuples containing each element and its length"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """create a element length function"""
    return [(i, len(i)) for i in lst]
