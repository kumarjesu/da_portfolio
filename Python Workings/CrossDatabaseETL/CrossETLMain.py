import GetOnlineData as gt
import PostgresUpload as up
import pandas as pd

## TO LOAD THE DATA FROM THE SNOW FLAKES ##
#gt.getSnowflakesData()

## TO UPLOAD THE SNOWFLAKES DATA IN POSTGRES DATABASE (DOCKER) ##
#up.uploadinpostgresql()


df = pd.read_csv('files/ToyotaCorolla.csv')
df.head()