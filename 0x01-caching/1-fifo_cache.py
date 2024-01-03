#!/usr/bin/env python3
"""Basic Cache System"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching System"""

    def __init__(self) -> None:
        super().__init__()
        self.cached_keys = []

    def put(self, key: str, item: str) -> None:
        """puts item to cache"""
        if key and item:
            self.cache_data[key] = item
            self.cached_keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.cached_keys[0]]
                print(f"DISCARD: {self.cached_keys[0]}")
                self.cached_keys.pop(0)

    def get(self, key: str) -> str:
        """gets cached item"""
        if key:
            return self.cache_data.get(key)
