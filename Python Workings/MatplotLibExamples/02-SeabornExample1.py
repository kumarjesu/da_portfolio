import matplotlib as plt
import seaborn as sns

tips = sns.load_dataset("tips")
#print(tips.head())

sns.set_style("white")
sns.scatterplot(data=tips, x="total_bill", y="tip")