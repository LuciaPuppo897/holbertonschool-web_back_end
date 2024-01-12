#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""

from typing import Tuple

def index_range(page: int , page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index
