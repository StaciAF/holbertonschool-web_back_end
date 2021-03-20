#!/usr/bin/env python3
"""
this module creates a new class BasicCache inherited from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ this class inherits from BaseCaching """
    def put(self, key, item):
        """ class method to put item in cache dict """
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ class method to return a value from cache dict """
        return self.cache_data.get(key)
