import snowflake.connector
import pandas as pd
import os
import csv
from dotenv import load_dotenv
from snowflake.connector import DictCursor

def getSnowflakesData():
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
        query = "SELECT * FROM CUSTOMER_ADDRESS WHERE LIMIT 10000"
        qry = '''SELECT c.c_customer_id, c.c_salutation, c.c_first_name, c.c_last_name, c.c_birth_day, c.c_birth_month, c.c_birth_year, c.c_birth_country, 
                    ca.ca_city, ca.ca_county, ca.ca_zip, ca.ca_location_type
                FROM customer c
                INNER JOIN 
                    customer_address ca
                ON
                    c.c_current_addr_sk = ca.ca_address_sk
                AND 
                    c.c_birth_country = 'UNITED KINGDOM'
                LIMIT 50000
    '''

        cursor.execute(qry)
        results = cursor.fetchall()
        df = pd.DataFrame(results)
        print(df.count())
        filename = "customer_uk.csv"
        outdir = "files"
        df.to_csv(f"{outdir}/{filename}", index=False)

    except Exception as exc:
        print(exc)
    finally:
        sf_connect.close()

