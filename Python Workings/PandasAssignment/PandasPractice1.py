import pandas as pd
import numpy as np

# Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), columns=['A', 'B', 'C', 'D'])
print("Original DataFrame:")
print(df)

# Set the index to be the first column
df.set_index('A', inplace=True)
print("DataFrame with new index:")
print(df)
print()
# Create a Pandas DataFrame with specified columns and index
df = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), columns=['A', 'B', 'C'], index=['X', 'Y', 'Z'])
print("Original DataFrame:")
print(df)

# Access the element at row 'Y' and column 'B'
element = df.at['Y', 'B']
print("Element at row 'Y' and column 'B':", element)