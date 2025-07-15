
from pymongo import MongoClient, ReturnDocument

connString = "mongodb://admin:Augusta%401407@localhost:27017/"
localClient = MongoClient(connString)

# ACCESS THE DB & COLLECTION
db = localClient['javaspringboot']
collections = db['person']

localClient.close()
'''
# READ ALL DOCUMENTS
for doc in allDocuments:
    print(doc)


# INSERT ONE DOCUMENT INTO COLLECTIONS
insertDocument = {
'_id': 125, 'firstName': 'Kingsly', 'lastName': 'Azariah', 'gender': 'Male', 'age': 40,
    'courses': ['Java', 'AI', 'Golang'],
    'address': [{'doorNo': 45, 'street': 'Lords Street', 'area': 'Halifax', 'county': 'London'}]
}

result = collections.insert_one(insertDocument)
print(result.inserted_id)


# INSERT MULTIPLE DOCUMENT INTO COLLECTIONS
multipleDocument = [
{
'_id': 201, 'firstName': 'Anwar', 'lastName': 'xxx', 'gender': 'Male', 'age': 42,
    'courses': ['C#', '.Net', 'Azure'],
    'address': [{'doorNo': 1055, 'street': 'Dubai Street', 'area': 'Al Buhari', 'county': 'Dubai'}]
},
{
'_id': 202, 'firstName': 'Jawahar', 'lastName': 'xxx', 'gender': 'Male', 'age': 42,
    'courses': ['Python', 'Django', 'GCB'],
    'address': [{'doorNo': 452, 'street': 'Malahal Street', 'area': 'Manosair', 'county': 'Singapore'}]
}
]

result = collections.insert_many(multipleDocument)
print(result)


# FIND ALL THE DOCUMENTS / RECORDS IN DB
allDocuments = collections.find()

print("Add a document : ")
insertDocument = {
'_id': 1250, 'firstName': 'Test', 'lastName': 'TEST', 'gender': 'Male', 'age': 00,
    'courses': ['Test', 'Test', 'Test'],
    'address': [{'doorNo': 00, 'street': 'Test Street', 'area': 'Test', 'county': 'Test'}]
}
result = collections.insert_one(insertDocument)
print(result)
print()

# FIND A SPECIFIC DOCUMENT
print("Find a document : ")
document = collections.find_one({"firstName":"Test"})
print(document)
print()

# FIND A SPECIFIC DOCUMENT AND UPDATE
print("Find a document and update : ")
print(collections.find_one_and_update(
    {'firstName':'Test'},
     {'$set' : {'firstName':'John'}},
    return_document=ReturnDocument.AFTER
))
print()

# FIND A SPECIFIC DOCUMENT AND REPLACE
print("Find a document and replace : ")
print(collections.find_one_and_replace(
    {'lastName':'TEST'},
    {'lastName':'David'},
    return_document=ReturnDocument.AFTER
))
print()

# FIND A SPECIFIC DOCUMENT AND DELETE
print("Find a document and delete : ")
print(collections.find_one_and_delete(
    {'firstName':'John'}
))
print()

'''
