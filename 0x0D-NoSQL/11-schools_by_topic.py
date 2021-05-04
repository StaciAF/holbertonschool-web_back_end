#!/usr/bin/env python3
"""
this module adds operations on db to be passed to MongoDB
"""


def schools_by_topic(mongo_collection, topic):
    """ this method returns list of schools based on topic """
    return mongo_collection.find({"topics": topic})
