import snowflake.connector
import os
from dotenv import load_dotenv

def loadDate2Snowflake():
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
        sf_connect

        sf_connect.cursor().execute("DROP DATABASE PythonSnowflakeDb")
        print("Existing Database Dropped !!!!")

        sf_connect.cursor().execute("CREATE DATABASE IF NOT EXISTS PythonSnowflakeDb ")
        print("Database Re-Created !!!")

        sf_connect.cursor().execute("USE DATABASE PythonSnowflakeDb")
        print("Path set to created database !!!")

        tableQuery = """
            CREATE TABLE IF NOT EXISTS Diamonds (
            carat DECIMAL(10,3) NOT NULL,
            cut VARCHAR(20) NOT NULL,
            color VARCHAR(5) NOT NULL,
            clarity VARCHAR(10) NOT NULL,
            depth DECIMAL(10,3) NOT NULL,
            tables DECIMAL(10,3) NOT NULL,
            price DECIMAL(10,3) NOT NULL,
            tagx DECIMAL(10,3) NOT NULL,
            tagy DECIMAL(10,3) NOT NULL,
            tagz DECIMAL(10,3) NOT NULL
            )
        """

        sf_connect.cursor().execute(tableQuery)
        print("Table created !!!!")

        sf_connect.cursor().execute(r"put file://C:/Users/kamal/PycharmProjects/NumpyPandasExample/files/Diamonds.csv @%Diamonds parallel=6")
        print("Copy the Diamonds.csv file from local directory to Snowflake Environment !!!!")

        sf_connect.cursor().execute("list @%Diamonds")
        print("List the files in DiamondFiles")

        sf_connect.cursor().execute("create file format PythonSnowflakeDb.PUBLIC.CSV_FILE type=csv")
        print("File Format Created for csv file !!!!")

        sf_connect.cursor().execute("COPY INTO Diamonds from @%Diamonds file_format=PythonSnowflakeDb.PUBLIC.CSV_FILE")
        print("Uploaded Successfully in Snowflakes Database !!!!!")

    except Exception as exc:
        print(exc)
    finally:
        sf_connect.close()