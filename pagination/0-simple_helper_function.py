#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for a given page and page size.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be greater than zero.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index
