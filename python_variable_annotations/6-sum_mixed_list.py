#!/usr/bin/env python3
"""Returns the sum of integers and floats in the given mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
