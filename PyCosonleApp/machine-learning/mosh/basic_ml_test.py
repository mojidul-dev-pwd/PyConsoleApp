##import pandas as pd
##df = pd.read_csv("vgsales.csv")
##print(df)
#total line and no of column
##df.shape
#show details data min, max, std, mean etc
##df.describe()
#values from the first row
##df.values

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_df = pd.read_csv("music.csv")
X = music_df.drop(columns=["genre"])
y = music_df["genre"]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
#X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.8)

model = DecisionTreeClassifier()
#model.fit(X,y)
#predictions = model.predict([[21,1],[22,0]])

model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)
print(score)

"""

"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

music_df = pd.read_csv("music.csv")
X = music_df.drop(columns=["genre"])
y = music_df["genre"]

model = DecisionTreeClassifier()
model.fit(X,y)
joblib.dump(model, 'music-recommender.joblib')
"""

"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

music_df = pd.read_csv("music.csv")
X = music_df.drop(columns=["genre"])
y = music_df["genre"]

model = DecisionTreeClassifier()
model.fit(X,y)
model = joblib.load('music-recommender.joblib')
predictions = model.predict([[21,1]])
print(predictions)

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_df = pd.read_csv("music.csv")
X = music_df.drop(columns=["genre"])
y = music_df["genre"]

model = DecisionTreeClassifier()
model.fit(X,y)

tree.export_graphviz(model, out_file='music-recommender.dot',
                     feature_names=['age','gender'],
                     class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)




