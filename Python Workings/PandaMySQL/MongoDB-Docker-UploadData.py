import json
import pandas as pd
import os

from pymongo import MongoClient

#client = MongoClient("mongodb+srv://admin:Augusta1407@pythonawscluster.1fclqc7.mongodb.net/?retryWrites=true&w=majority&appName=PythonAWSCluster")
connString = "mongodb://admin:Augusta%401407@localhost:27017/"
localClient = MongoClient(connString)

db = localClient['db_mongo']
collections = db['airlinesCollection']

outdir = 'files'
if not os.path.exists(outdir):
    os.mkdir(outdir)

dframe = pd.read_csv(f"{outdir}/{"airlines_final.csv"}")
dframe.to_json(f"{outdir}/{"airlines_final.json"}", index=False)

with open('files/airlines_final.json', 'r') as file:
    data = json.load(file)
    if isinstance(data, list):
        collections.insert_many(data)
    else:
        collections.insert_one(data)
    print("Data imported successfully !!!!")

localClient.close()