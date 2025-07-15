import pandas as pd
import os

from sqlalchemy import create_engine, text

dbConString = "mysql+mysqlconnector://{USER}:{PWD}@{HOST}/{DBNAME}"

dbConString = dbConString.format(
    USER = "admin", PWD = "Jazlyn0910", HOST="localhost:3306", DBNAME="pythontraining"
)

engine = create_engine(dbConString, echo=False)
try:
    with engine.begin() as dbConString:
        dframe = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

        outdir = 'files'
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        dframe.to_csv(f"{outdir}/{"Diamonds.csv"}", index=False)

        dframe.to_sql(
            name="tbl_diamonds",
            if_exists='append',
            con=dbConString
        )

        sql_query = text("""
                    select cut, color, count(*) from pythontraining.tbl_diamonds
                    group by cut, color
                    order by cut, color
                    """)

        cut_color_count = pd.read_sql_query(
            sql=sql_query,
            con=dbConString
        )
        print(cut_color_count)
finally:
    dbConString.close()