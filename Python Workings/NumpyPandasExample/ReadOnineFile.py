import pandas as pd
import os

def loadData():
    try:
        dframe = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
        outdir = 'files'
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        dframe.to_csv(f"{outdir}/{"Diamonds.csv"}", index=False)
    except Exception as exc:
        print(exc)
    finally:
        return dframe