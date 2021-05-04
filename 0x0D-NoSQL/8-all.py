#!/usr/bin/env python3
"""
this module adds operations on db to be passed to MongoDB
"""


def list_all(mongo_collection):
    """ this function lists all docs in a collection """
    if mongo_collection:
        return mongo_collection.find()
    else:
        return []
