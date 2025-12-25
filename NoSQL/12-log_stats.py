#!/usr/bin/env python3
"""Log stats module."""
from pymongo import MongoClient

if __name__ == "__main__":
    # MongoDB-yə qoşulma
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. Ümumi sənəd sayını tapmaq
    n_logs = nginx_collection.count_documents({})
    print(f"{n_logs} logs")

    # 2. Metodlar üzrə statistika
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Status check (method=GET və path=/status) sayını tapmaq
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
