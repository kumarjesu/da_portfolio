import pandas as pd
import os

from sqlalchemy import create_engine, text
from dotenv import load_dotenv


try:
    # ESTABLISH CONNECTIONS
    dbConnectionString = "postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"

    # OS ENVIRONMENT
    #dbUser=os.environ.get('DOCKER_POSTGRES_USERNAME')
    #dbPass=os.environ.get('DOCKER_POSTGRES_PASSWORD')

    # USING python-dotenv
    # Step 1: pip install python-dotenv :::: Step 2: Create a .env file and save the necessary values.
    # Step 3: from dotenv import load_dotenv :::: Step 4: import os ::: Step 5. load_dotenv()

    load_dotenv()

    dbUser = os.environ.get("POSTGRES_USERNAME")
    dbPass = os.environ.get("POSTGRES_PASSWORD")
    dbDbase= os.environ.get("POSTGRES_DATABASE")
    dbPort = os.environ.get("POSTGRES_PORT")
    dbHost= os.environ.get("POSTGRES_HOST")

    #print(dbUser)
    #print(dbPass)

    # LOCAL MACHINE PGADMING
    #dbConnectionString = dbConnectionString.format(
    #    USER="postgres", PASSWORD="Jerrick2911", HOST="localhost",PORT="5433", DBNAME="airlinesdb")

    # DOCKER CONTAINER
    dbConnectionString = dbConnectionString.format(
        USER=dbUser, PASSWORD=dbPass, HOST=dbHost,PORT=dbPort, DBNAME=dbDbase)

    engine = create_engine(dbConnectionString, echo=False)

    with engine.begin() as dbConnectionString:
        # IMPORT THE CSV FILE TO CREATE A DATAFRAME
        outdir = 'files'
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        dframe = pd.read_csv(f"{outdir}/{"airlines_final.csv"}")

        dframe.to_sql('airlines_details', dbConnectionString, if_exists='replace', index=False)

finally:
    dbConnectionString.commit()
    dbConnectionString.close()