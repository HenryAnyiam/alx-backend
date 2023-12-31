#!/usr/bin/env python3
"""Implement a helper function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """a helper function to return offset"""
    index = (page - 1) if page > 0 else page
    return ((index * page_size), (page * page_size))
