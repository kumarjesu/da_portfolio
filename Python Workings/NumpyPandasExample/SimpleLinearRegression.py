from sklearn.metrics import r2_score

import LoadSnowflakesData
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = LoadSnowflakesData.loadData()

df.head()
# print(df.head()) # DISPLAYS THE FIRST 5 RECORDS FROM 0-4
df.tail()
# print(df.tail()) # DISPLAYS THE LAST 5 RECORDS

columned_df = df[['CR_RETURN_AMOUNT','CR_NET_LOSS']]

filtered_df = columned_df[(columned_df['CR_RETURN_AMOUNT']>1000) & (columned_df['CR_NET_LOSS'] > 0)]
#print(filtered_df.count())
#print(filtered_df)

# COLUMN CR_RETURN_AMOUNT
X = filtered_df.iloc[:, :-1].values
#print(X)

# COLUMN CR_NET_LOSS
y = filtered_df.iloc[:, -1].values
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

regressor.predict(np.array([[1800]]))

accuracy = regressor.score(X_test,y_test)
r2_score(y_test,y_pred)

print(accuracy)
print(accuracy*100,'%')

X_test1=np.array([[2500],[3750]])
X_test1

y_pred1 = regressor.predict(X_test1)
print(y_pred1)