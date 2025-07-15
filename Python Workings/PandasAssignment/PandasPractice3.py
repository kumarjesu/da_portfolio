import pandas as pd
import numpy as np

# Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers
df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)), columns=['A', 'B', 'C'])
print("Original DataFrame:")
print(df)

# Introduce some NaN values
df.iloc[0, 1] = np.nan
df.iloc[2, 2] = np.nan
df.iloc[4, 0] = np.nan
print("DataFrame with NaN values:")
print(df)

# Fill the NaN values with the mean of the respective columns
df.fillna(df.mean(), inplace=True)
print("DataFrame with NaN values filled:")
print(df)

print()

# Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), columns=['A', 'B', 'C', 'D'])
print("Original DataFrame:")
print(df)

# Introduce some NaN values
df.iloc[1, 2] = np.nan
df.iloc[3, 0] = np.nan
df.iloc[5, 1] = np.nan
print("DataFrame with NaN values:")
print(df)

# Drop the rows with any NaN values
df.dropna(inplace=True)
print("DataFrame with NaN values dropped:")
print(df)