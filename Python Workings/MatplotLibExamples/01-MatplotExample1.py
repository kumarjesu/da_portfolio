import pandas as pd
import matplotlib.pyplot as plt
import os

outdir = 'files'
if not os.path.exists(outdir):
    os.mkdir(outdir)

airlinedf = pd.read_csv(f"{outdir}/{"airlines_final.csv"}")
fooddf = pd.read_csv(f"{outdir}/{"food.csv"}")

xVal1 = airlinedf.airline
xVal2 = fooddf.item_name

'''
# TOP 10 ITEMS
print(airlinedf.head(10))

# ALL airline COUNT
print(xVal1.value_counts())
print()

# SORT THE VALUES FROM THE OP TO THE LEAST VALUE AND SLICE THE FIRST 10 ITEMS
data = xVal1.sort_values(ascending=True)
print(data.head(10))
print()

# TOP 5/10 ITEMS OF FIELD WISE
top5 = xVal1.value_counts().head()
top10 = xVal1.value_counts().head()
print(top5)

# FOR BAR GRAPH
top5.plot(kind='bar')
plt.xlabel('Airlines')
plt.ylabel('No of Travel')
plt.title('Top 5 Airlines')
plt.show()

# FOR LINE GRAPH
top5.plot(kind='line')
plt.xlabel('Airlines')
plt.ylabel('No of Travel')
plt.title('Top 5 Airlines')
plt.show()
'''

agroup = airlinedf.groupby('airline').sum()
orders = fooddf.groupby('item_name').sum()


plt.scatter(x = orders.item_price1, y=orders.quantity, s=60, c='blue')
plt.xlabel('Order Prices')
plt.ylabel('Items Ordered')
plt.title('No of items ordered per order price')
plt.ylim(0)
plt.show()