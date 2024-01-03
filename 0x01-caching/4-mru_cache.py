#!/usr/bin/env python3
"""Basic Cache System"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Most Recently Used
    Caching System
    """

    def __init__(self) -> None:
        super().__init__()
        self.key_list = []

    def put(self, key: str, item: str) -> None:
        """puts item to cache"""
        if key and item:
            if ((len(self.cache_data) == self.MAX_ITEMS)
               and (key not in self.key_list)):
                discarded = self.key_list.pop(-1)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            if key in self.key_list:
                self.key_list.remove(key)
            self.key_list.append(key)

    def get(self, key: str) -> str:
        """gets cached item"""
        if key:
            if key in self.key_list:
                self.key_list.remove(key)
                self.key_list.append(key)
            return self.cache_data.get(key)
