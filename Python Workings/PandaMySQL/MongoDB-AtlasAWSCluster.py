import json
import pandas as pd
import os

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:Augusta1407@pythonawscluster.1fclqc7.mongodb.net/?retryWrites=true&w=majority&appName=PythonAWSCluster")

db = client['db_mongo']
collections = db['diamondsCollection']

dframe = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

outdir = 'files'
if not os.path.exists(outdir):
    os.mkdir(outdir)

dframe.to_json(f"{outdir}/{"diamonds.json"}", index=False)

with open('files/diamonds.json', 'r') as file:
    data = json.load(file)
    if isinstance(data, list):
        collections.insert_many(data)
    else:
        collections.insert_one(data)
    print("Data imported successfully !!!!")

client.close()




