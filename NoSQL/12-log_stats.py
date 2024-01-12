#!/usr/bin/env python3
"""
    Write a Python script that provides some stats
    about Nginx logs stored in MongoDB:

"""

import pymongo


def nginx_logs_stats(mongo_collection):
    """Total number of logs"""
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    count_status = mongo_collection.count_documents({"method":
                                                    "GET", "path": "/status"})
    print(f"{count_status} status check")
