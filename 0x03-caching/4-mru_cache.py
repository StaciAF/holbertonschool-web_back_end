#!/usr/bin/env python3
"""
this module creates a class MRUCache inherited from BaseCaching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ this class is a MOST RECENTLY USED caching system  """
    getList = []
    putList = []

    def __init__(self):
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ edits cache based on MRU method """
        if key and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            self.putList.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removeG = self.getList[-1]
                removeP = self.putList[-1]
                if removeG in self.cache_data:
                    print('DISCARD: ' + str(removeG))
                    del self.cache_data[removeG]
                else:
                    removeP = self.putList[-2]
                    print('DISCARD: ' + str(removeP))
                    del self.cache_data[removeP]

    def get(self, key):
        """ class method to return a value from cache dict """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.getList.append(key)
            return self.cache_data[key]
