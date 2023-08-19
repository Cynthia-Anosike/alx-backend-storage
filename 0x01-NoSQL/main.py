#!/usr/bin/env python3
''' A mongoDB with python's learners page'''

from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
# create a database 'post'
db = client["bookshelf"]
book1 = {
    "title": "Killing Eve",
    "author": "Magerate Spender",
    "contributors": [
        "Mathar Lazarus",
        "Alex Adren",
        "Faith Latty"
    ],
    "url": "www.killingeve.com",
}
book2 = {
    "title": "House on the dragon",
    "author": "James Rodriguez",
    "contributors": [
        "Aldof Hitler",
        "Jack Putin"
    ],
    "url": "www.HBO.com",
}
# Create a collection and insert the dictionary as documents
book = db.books
result = book.insert_many([book1, book2])
print(f"Multiple Books: {result.inserted_ids}")

for doc in book.find():
    print(f"\n\n{doc}")
