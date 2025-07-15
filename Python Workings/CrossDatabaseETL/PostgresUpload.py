import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


def uploadinpostgresql():
    try:

        # DOCKER CONTAINER PGADMIN IN PORT 5200
        # ESTABLISH CONNECTIONS
        dbConnectionString = "postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"

        load_dotenv()

        dbUser = os.getenv("POSTGRES_USERNAME")
        dbPass = os.getenv("POSTGRES_PASSWORD")
        dbDbase = os.getenv("POSTGRES_DATABASE")
        dbPort = os.getenv("POSTGRES_PORT")
        dbHost = os.getenv("POSTGRES_HOST")

        # LOCAL POSTGRES
        dbConnectionString = dbConnectionString.format(
            USER=dbUser, PASSWORD=dbPass, HOST=dbHost, PORT=dbPort, DBNAME=dbDbase)

        engine = create_engine(dbConnectionString, echo=False)

        with engine.begin() as dbConnectionString:
            # IMPORT THE CSV FILE TO CREATE A DATAFRAME
            outdir = 'files'
            if not os.path.exists(outdir):
                os.mkdir(outdir)

            dframe = pd.read_csv(f"{outdir}/{"customer_uk.csv"}")

            ## SEGREGATE THE DATA BASED ON CUT
            dframe.to_sql('tbl_UK_Customers', dbConnectionString, if_exists='replace', index=False)

    finally:
        dbConnectionString.commit()
        dbConnectionString.close()