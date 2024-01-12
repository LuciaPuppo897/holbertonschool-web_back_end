#!/usr/bin/env python3
"""
    List all documents in a MongoDB collection.
    :param mongo_collection: pymongo collection object
    :return: List of documents in the collection
"""


def list_all(mongo_collection):
    """function that return an empty list if no doc found"""
    documents = list(mongo_collection.find({}))
    return documents
