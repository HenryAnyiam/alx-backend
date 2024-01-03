#!/usr/bin/env python3
"""Basic Cache System"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching System"""

    def __init__(self) -> None:
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """puts item to cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """gets cached item"""
        if key:
            return self.cache_data.get(key)
