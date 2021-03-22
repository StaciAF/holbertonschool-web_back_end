#!/usr/bin/env python3
"""
this module creates a class LFUCache inherited from BaseCaching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ this class is a LAST FREQUENTLY USED caching system  """
    def __init__(self):
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ edits cache based on LFU method """
        if key and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                remove = self.cache_data.popitem(last=False)
                print('DISCARD: ' + str(remove[0]))

    def get(self, key):
        """ class method to return a value from cache dict """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
