#!/usr/bin/env python3
"""
this module creates a class FIFOcache inherited from BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ this class is a FIRST IN FIRST OUT caching system  """
    cache_list = []

    def put(self, key, item):
        """ edits cache based on FIFO method """
        if key and item is not None:
            self.cache_data[key] = item
            if key not in self.cache_list:
                self.cache_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                remove = self.cache_list.pop(0)
                print('DISCARD: ' + remove)
                del self.cache_data[remove]

    def get(self, key):
        """ class method to return a value from cache dict """
        return self.cache_data.get(key)
