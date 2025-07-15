import snowflake.connector
import os

try:
    uname = os.environ.get("USER_NAME")
    pwd = os.environ.get("PASSWORD")
    acc = os.environ.get("ACCOUNT")
    whouse = os.environ.get("WAREHOUSE")

    sf_connect = snowflake.connector.connect(
        user=uname,
        password=pwd,
        account=acc,
        warehouse=whouse
    )

    sf_connect

    sf_connect.cursor().execute("DROP DATABASE PythonSnowflakeDb")
    print("Existing Database Dropped !!!!")

    sf_connect.cursor().execute("CREATE DATABASE IF NOT EXISTS PythonSnowflakeDb ")
    print("Database Re-Created !!!")

    sf_connect.cursor().execute("USE DATABASE PythonSnowflakeDb")
    print("Path set to created database !!!")

    tableQuery = """
        CREATE TABLE IF NOT EXISTS FundServices (
        Reporting_Period VARCHAR(10) NOT NULL,
        Holder_Sector VARCHAR(10) NOT NULL,
        Instrument_Type VARCHAR(50) NOT NULL,
        Issuer_Region VARCHAR(50) NOT NULL,
        Issuer_Sector VARCHAR(10) NOT NULL,
        Nominal_Currency VARCHAR(15) NOT NULL,
        Original_Maturity VARCHAR(15) NOT NULL,
        Holding_Amount DECIMAL(25,2) NOT NULL
        )
    """

    sf_connect.cursor().execute(tableQuery)
    print("Table created !!!!")

    sf_connect.cursor().execute(r"put file://C:/Users/kamal/PycharmProjects/SnowflakeExample/files/Shares.csv @%FundServices parallel=6")
    print("Copy the Shares.csv file from local directory to Snowflake Environment !!!!")

    #sf_connect.cursor().execute("list @%FundServices")
    #print("List the files in FundServices")

    sf_connect.cursor().execute("create file format PythonSnowflakeDb.PUBLIC.CSV_FILE type=csv")
    print("File Format Created for csv file !!!!")

    sf_connect.cursor().execute("COPY INTO FundServices from @%FundServices file_format=PythonSnowflakeDb.PUBLIC.CSV_FILE")
    print("Uploaded Successfully in Snowflakes Database !!!!!")

except Exception as exc:
    print(exc)
finally:
    sf_connect.close()