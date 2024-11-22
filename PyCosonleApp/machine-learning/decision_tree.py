#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

#Decision Tree
df = pandas.read_csv("dataset.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
#   print(df)

# X is the feature columns,
# y is the target column
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

#print(X)
#print(y)

#Now we can create the actual decision tree, fit it with our details.
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features)

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

"""
The Gini method uses this formula
Gini = 1 - (x/n)2 - (y/n)2
"""
print('')
print('predict value',dtree.predict([[40, 10, 7, 1]]))
print("[1] means 'GO' and [0] means 'NO'")
print(dtree.predict([[40, 10, 6, 1]]))

"""
You will see that the Decision Tree gives you different results 
if you run it enough times, even if you feed it with the same data.
That is because the Decision Tree does not give us a 100% certain answer. 
It is based on the probability of an outcome, and the answer will vary.
"""
