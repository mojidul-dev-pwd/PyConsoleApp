import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#%matplotlib inlinne
"""
df = pd.read_csv('../files/USA_Housing.csv')
print(df.head())
print(df.info())
print(df.columns)
sns.pairplot(df)
sns.distplot(df['Price'])
df.corr()
sns.heatmap(df.corr())
"""
## x-axis represents age, and the y-axis represents speed
x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, relation, predict, std_err = stats.linregress(x1,y1)
print("slope", slope)
print("intercept", intercept)
print("relation", relation)
print("predict", predict)
print("std_err", std_err)
def myfunc(x1):
  return slope * x1 + intercept
## Predict the speed of a 10 years old car
speed = myfunc(10)
print("speed", speed)

mymodel = list(map(myfunc, x1))

## shows existing data
plt.scatter(x1, y1)
## Draw a linear regression line
plt.plot(x1, mymodel)
# shows figure
plt.show()

