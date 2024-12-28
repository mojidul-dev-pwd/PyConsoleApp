import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# data
data_set = pd.read_csv("test_data.csv")
x= data_set.iloc[:, :-1].values
y= data_set.iloc[:, 1].values

X_train, X_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)

model = LinearRegression()
model.fit(X_train,y_train)

#Prediction of Test and Training set result
y_predictions = model.predict(X_test)
x_predictions = model.predict(X_train)

plt.scatter(X_train, y_train, color="green")
plt.plot(X_train, x_predictions, color="red")
plt.title("Salary vs Experience (Training Dataset)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary(In BDT)")
plt.show()

#visualizing the Test set results
plt.scatter(X_test, y_test, color="blue")
plt.plot(X_train, x_predictions, color="red")
plt.title("Salary vs Experience (Test Dataset)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary(In BDT)")
plt.show()


