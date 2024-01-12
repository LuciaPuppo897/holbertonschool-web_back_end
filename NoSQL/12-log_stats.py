#!/usr/bin/env python3
"""
    Write a Python script that provides some stats
    about Nginx logs stored in MongoDB:

"""


from pymongo import MongoClient


if __name__ == "__main__":
    """main function"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    print("{} logs".format(log_collection.count_documents({})))
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for m in method:
        print('\tmethod {}: {}'.format(
            m, log_collection.count_documents({"method": m})))

    print("{} status check".format(log_collection.count_documents(
        {"method": "GET", "path": "/status"})))
