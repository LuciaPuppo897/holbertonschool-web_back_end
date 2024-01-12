#!/usr/bin/env python3
"""
function that changes all topics of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Update documents with the given school name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
