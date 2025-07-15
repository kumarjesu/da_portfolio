import pandas as pd
import os


dframe = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

general1 = (dframe[(dframe['carat']>1.00) & (dframe['price']>7500)]).sort_values(by='cut')
general2 = (dframe[(dframe['carat'].between(0.50,1.00)) ]).sort_values(by='cut')
general3 = (dframe[(dframe['carat'].between(0.00,0.50))]).sort_values(by='cut')

outdir = 'files'
if not os.path.exists(outdir):
    os.mkdir(outdir)

general1.to_csv(f"{outdir}/{"Diamonds1.csv"}",index=False)
general2.to_csv(f"{outdir}/{"Diamonds2.csv"}",index=False)
general3.to_csv(f"{outdir}/{"Diamonds3.csv"}",index=False)


