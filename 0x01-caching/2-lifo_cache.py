#!/usr/bin/env python3
"""Basic Cache System"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching System"""

    def __init__(self) -> None:
        super().__init__()
        self.cached_keys = []

    def put(self, key: str, item: str) -> None:
        """puts item to cache"""
        if key and item:
            if ((len(self.cache_data) == BaseCaching.MAX_ITEMS)
               and (key not in self.cached_keys)):
                del self.cache_data[self.cached_keys[-1]]
                print(f"DISCARD: {self.cached_keys[-1]}")
                self.cached_keys.pop()
            self.cache_data[key] = item
            self.cached_keys.append(key)

    def get(self, key: str) -> str:
        """gets cached item"""
        if key:
            return self.cache_data.get(key)
