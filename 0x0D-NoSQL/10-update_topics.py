#!/usr/bin/env python3
"""
this module adds operations on db to be passed to MongoDB
"""


def update_topics(mongo_collection, name, topics):
    """ this method changes all topics in docs by name """
    mongo_collection.update_many({"name": name}, {'$set': {"topics": topics}})
