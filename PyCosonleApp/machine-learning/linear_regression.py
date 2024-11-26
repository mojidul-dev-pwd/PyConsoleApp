import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inlinne

df = pd.read_csv('../files/USA_Housing.csv')
print(df.head())
print(df.info())
print(df.columns)
sns.pairplot(df)
sns.distplot(df['Price'])
df.corr()
sns.heatmap(df.corr())
