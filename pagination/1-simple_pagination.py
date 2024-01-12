#!/usr/bin/env python3
"""Implement a method named get_page
that takes two integer arguments page
with default value 1 and page_size with default value 10
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page function"""
        assert (type(page), type(page_size)) == (int, int)
        assert page > 0
        assert page_size > 0

        data = self.dataset()
        index = index_range(page, page_size)

        if index[1] > len(data):
            return []
        return data[index[0]:index[1]]
