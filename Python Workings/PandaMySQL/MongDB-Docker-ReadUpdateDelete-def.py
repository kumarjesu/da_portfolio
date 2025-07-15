import pandas as pd

from pymongo import MongoClient, ReturnDocument


# READ ALL DOCUMENTS / RECORDS IN DB
def readllDocuments():
    allDocuments = collections.find()
    for doc in allDocuments:
        print(doc)


# READ DOCUMENTS / RECORDS IN DB BY SPECIFIC COLUMN
def readDocumentsByName(fname):
    document = collections.find_one({"firstName": fname})
    print(document)
    print()


# INSERT SINGLE DOCUMENT INTO COLLECTIONS
def insertOneDocument():
    insertDocument = {
        '_id': 222, 'firstName': 'Josy', 'lastName': 'Joy', 'gender': 'Male', 'age': 40,
        'courses': ['Java', 'AI', 'Golang'],
        'address': [{'doorNo': 45, 'street': 'Lords Street', 'area': 'Halifax', 'county': 'London'}]
    }

    result = collections.insert_one(insertDocument)
    print(result.inserted_id)


# INSERT MULTIPLE DOCUMENT INTO COLLECTIONS
def insertMultipleDocument():
    multipleDocument = [
        {
            '_id': 333, 'firstName': 'Kalivaradhan', 'lastName': 'xxx', 'gender': 'Male', 'age': 42,
            'courses': ['AI', 'Golang', 'Google Cloud'],
            'address': [{'doorNo': 2241, 'street': 'Henry Street', 'area': 'Washington DC', 'county': 'USA'}]
        },
        {
            '_id': 444, 'firstName': 'Senthil', 'lastName': 'xxx', 'gender': 'Male', 'age': 42,
            'courses': ['C++', 'Java', 'AWS'],
            'address': [{'doorNo': 1452, 'street': 'Temple Street', 'area': 'Kulalampur', 'county': 'Singapore'}]
        }
    ]

    result = collections.insert_many(multipleDocument)
    print(result)


def updateDocument():
    # FIND A SPECIFIC DOCUMENT AND UPDATE
    print("Find a document and update : ")
    print(collections.find_one_and_update(
        {'firstName': 'Test'},
        {'$set': {'firstName': 'John'}},
        return_document=ReturnDocument.AFTER
    ))
    print()

    # FIND A SPECIFIC DOCUMENT AND REPLACE
    print("Find a document and replace : ")
    print(collections.find_one_and_replace(
        {'lastName': 'TEST'},
        {'lastName': 'David'},
        return_document=ReturnDocument.AFTER
    ))
    print()

try:
    connString = "mongodb://admin:Augusta%401407@localhost:27017/"
    localClient = MongoClient(connString)

    # ACCESS THE DB & COLLECTION
    db = localClient['javaspringboot']
    collections = db['person']

    #readllDocuments()
    fname = input("Please enter the first Name : ")
    readDocumentsByName(fname)
    #insertOneDocument()
    #insertMultipleDocument()

finally:
    localClient.close()
