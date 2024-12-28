import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data_set = pd.read_csv("50_Startups.csv")
x= data_set.iloc[:, :-1].values
y= data_set.iloc[:, 4].values

#Catgorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x= LabelEncoder()
x[:, 3]= labelencoder_x.fit_transform(x[:,3])
onehotencoder= OneHotEncoder()
x= onehotencoder.fit_transform(x).toarray()
#avoiding the dummy variable trap:
x = x[:, 1:]

X_train, X_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)

#Fitting the MLR model to the training set:
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the Test set result;
y_predictions = regressor.predict(X_test)

print('Train Score: ', regressor.score(X_train, y_train))
print('Test Score: ', regressor.score(X_test, y_test))