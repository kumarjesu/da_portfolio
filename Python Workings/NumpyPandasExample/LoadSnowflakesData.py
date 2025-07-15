import snowflake.connector
import pandas as pd
import os
from dotenv import load_dotenv
from snowflake.connector import DictCursor

def loadData():
    try:
        load_dotenv()

        uname = os.getenv("USER_NAME")
        pwd = os.getenv("PASSWORD")
        acc = os.getenv("ACCOUNT")
        whouse = os.getenv("WAREHOUSE")
        dbase = os.getenv("DATABASE")
        schema = os.getenv("SCHEMA_NAME")

        sf_connect = snowflake.connector.connect(
            user=uname,
            password=pwd,
            account=acc,
            warehouse=whouse,
            database=dbase,
            schema=schema
        )

        cursor = sf_connect.cursor(DictCursor)
        query = "SELECT * FROM CATALOG_RETURNS LIMIT 1000"
        cursor.execute(query)
        results = cursor.fetchall()
        df = pd.DataFrame(results)
        print(df)
    except Exception as exc:
        print(exc)
    finally:
        sf_connect.close()
