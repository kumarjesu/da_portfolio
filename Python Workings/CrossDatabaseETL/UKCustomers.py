import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
sb.set_theme(color_codes=True)
pd.set_option('display.max_columns', None)

# READ THE UK CUSTOMER - csv
df = pd.read_csv('files/store.csv')
df.head()

df.nunique()

