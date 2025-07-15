
import snowflake.connector
import pandas as pd
import csv
import os
from variables import *

try:
    uname = "kamalrkumar"
    pwd = "Augusta@140776"
    acc = "HEBLJEQ-SN80974"
    whouse = "COMPUTE_WH"

    sf_connect = snowflake.connector.connect(
        user=uname,
        password=pwd,
        account=acc,
        warehouse=whouse
    )

    sf = sf_connect.cursor()

    query = "SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.CATALOG_RETURNS LIMIT 1000"
    #query = "SELECT TABLE_NAME,ROW_COUNT FROM SNOWFLAKE_SAMPLE_DATA.INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='TPCH_SF10' AND TABLE_TYPE='BASE TABLE'"
    #query = "SELECT TABLE_SCHEMA, TABLE_NAME, ROW_COUNT FROM SNOWFLAKE_SAMPLE_DATA.INFORMATION_SCHEMA.TABLES WHERE TABLE_CATALOG='SNOWFLAKE_SAMPLE_DATA' AND TABLE_TYPE='BASE TABLE'"
    sf.execute(query)

    counts = sf.fetchall()
    #print(counts)

    df = pd.DataFrame(counts)
    #print(df)

    #filename = "C:/Users/kamal/PycharmProjects/SnowflakeExample/files/SchemaCount.csv"
    #filename = "C:/Users/kamal/PycharmProjects/SnowflakeExample/files/TableRecCount.csv"
    filename = "C:/Users/kamal/PycharmProjects/SnowflakeExample/files/CatalogReturns.csv"
    with open(filename,'w',newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerows(counts)

except Exception as exc:
    print(exc)
finally:
    sf_connect.close()