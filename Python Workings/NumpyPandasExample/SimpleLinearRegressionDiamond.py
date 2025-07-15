import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import ReadOnineFile
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = ReadOnineFile.loadData()
cnt = df.count()

# FILTER DATA FRAME BASED ON CARAT AND PRICE
filter_df=df[(df['carat']>1.30)  & (df['price']>18500)]
cntGreater = filter_df.count()

# EXTRACT COUPLE OF COLUMNS TO ANOTHER DATAFRAME
linear_df1=filter_df[['carat','price']] # METHOD 1
linear_df2 = filter_df.filter(['carat','price']) # METHOD 2 - USING filter
linear_df3 = filter_df.iloc[:,[0,6]] # METHOD 3 USING -iloc

X = linear_df1.iloc[:, :-1].values
y = linear_df1.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)


regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

regressor.predict(np.array([[5.1]]))

accuracy = regressor.score(X_test,y_test)
r2_score(y_test,y_pred)

print(accuracy)
print(accuracy*100,'%')

 ## VISUALISING THE TRAINING SET RESULTS
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Carat vs Price (Training set)')
plt.xlabel('Diamond Carat')
plt.ylabel('Diamond Price')
plt.show()

## VISUALISING THE TEST SET RESULTS
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Carat vs Price (Training set)')
plt.xlabel('Diamond Carat')
plt.ylabel('Diamond Price')
plt.show()

X_test1=np.array([[1.95],[3.75]])
X_test1

y_pred1 = regressor.predict(X_test1)
print(y_pred1)