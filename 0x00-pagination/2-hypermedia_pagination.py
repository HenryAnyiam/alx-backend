#!/usr/bin/env python3
"""Implement a helper function
And handle pagination"""


import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """a helper function to return offset"""
    index = (page - 1) if page > 0 else page
    return ((index * page_size), (page * page_size))


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
        """paginate dataset for particular data"""
        assert isinstance(page, int) and\
               page > 0 and isinstance(page_size, int)\
               and page_size > 0
        offset = index_range(page, page_size)
        try:
            return self.dataset()[offset[0]:offset[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """use hypermedia metadata to paginate"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = (page + 1) if (page + 1) <= total_pages else None
        prev_page = (page - 1) if page > 1 else None
        return {'page_size': len(data), 'page': page,
                'data': data, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': total_pages}
