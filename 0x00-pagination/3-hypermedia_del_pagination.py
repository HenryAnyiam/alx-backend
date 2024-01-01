#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Union[int, None] = None,
                        page_size: int = 10) -> Dict:
        """implement deletion resillient pagination"""
        dataset = self.indexed_dataset()
        assert index and index < len(dataset)
        data: List = []
        indexed = False
        i = index
        next_page = index + page_size
        while len(data) != page_size:
            new = dataset.get(i)
            if new:
                data.append(new)
            i += 1
        next = None
        while not next:
            next = dataset.get(i)
            if not next:
                i += 1
        return {'index': index, 'next_index': i,
                'page_size': len(data), 'data': data}
