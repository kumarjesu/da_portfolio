import json
import pandas as pd
import requests
import os




json_link = "https://coderbyte.com/api/challenges/json/age-counting"

outdir = 'files'
if not os.path.exists(outdir):
    os.mkdir(outdir)

# LOAD DATA FROM THE https LINK
load_data = requests.get(json_link).json()
# print(type(data)) ## READING THE VALUE AS DICTIONARY
dframe = pd.DataFrame.from_dict(load_data,orient='index')
# CONVERT THE DATAFRAME INTO json file
dframe.to_json(f"{outdir}/{"age_counting.json"}", index=False)

# OPEN THE JSON FILE AND CONVERT IT AS csv file
with open('files/age_counting.json', 'r') as file:
    data = json.load(file)
    dframe = pd.DataFrame.from_dict(data,orient='index')
    dframe.to_csv(f"{outdir}/{"age_counting.csv"}", index=False)

    # print(type(data)) ## READING THE VALUE AS DICTIONARY
    #print(type(dframe))

