# 0x03. Caching
### Learning Objectives
  * What a caching system is
  * What FIFO means
  * What LIFO means
  * What LRU means
  * What MRU means
  * What LFU means
  * What the purpose of a caching system
  * What limits a caching system have

### More Info
**Parent class ``BaseCaching``**
All your classes must inherit from ``BaseCaching``

```
  $ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

### Tasks

#### 0. Basic dictionary
#### 1. FIFO caching
#### 2. LIFO Caching
#### 3. LRU Caching
#### 4. MRU Caching
#### 5. LFU Caching (advanced)
