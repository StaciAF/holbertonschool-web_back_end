#!/usr/bin/env python3
"""
this module adds operations on db to be passed to MongoDB
"""


def insert_school(mongo_collection, **kwargs):
    """ this method inserts a new doc in collection """
    doc = {}
    for key, val in kwargs.items():
        doc[key] = val
    inserted = mongo_collection.insert_one(doc)
    return inserted.inserted_id
