#!/usr/bin/env python3
"""Basic Cache System"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used
    Caching System
    """

    def __init__(self) -> None:
        super().__init__()
        self.key_list = []
        self.key_use = []

    def put(self, key: str, item: str) -> None:
        """puts item to cache"""
        if key and item:
            if ((len(self.cache_data) == self.MAX_ITEMS)
               and (key not in self.key_list)):
                lowest = self.key_list[0]
                val = self.key_use[0]
                index = 0
                for i in range(len(self.key_list)):
                    if val > self.key_use[i]:
                        val = self.key_use[i]
                        lowest = self.key_list[i]
                        index = i
                self.key_list.pop(index)
                self.key_use.pop(index)
                del self.cache_data[lowest]
                print(f"DISCARD: {lowest}")
            self.cache_data[key] = item
            val = 0
            if key in self.key_list:
                index = self.key_list.index(key)
                self.key_list.remove(key)
                val = self.key_use.pop(index)
            self.key_list.append(key)
            self.key_use.append(val + 1)

    def get(self, key: str) -> str:
        """gets cached item"""
        if key:
            if key in self.key_list:
                index = self.key_list.index(key)
                use = self.key_use[index]
                self.key_use.pop(index)
                self.key_use.append(use + 1)
                self.key_list.remove(key)
                self.key_list.append(key)
            return self.cache_data.get(key)
