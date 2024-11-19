"""
Mean - The average value
Median - The mid point value
Mode - The most common value
"""
import sys
#import matplotlib
#matplotlib.use('Agg')
import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print('mean =',x)
x = numpy.median(speed)
print('median =',x)
z = stats.mode(speed)
print('mode =',z)
#find out standard deviation using numpy module
x = numpy.std(speed)
print(x)
#A low standard deviation means that most of the numbers are close to the mean (average) value.
sp = [86,87,88,86,87,85,86]
x = numpy.std(sp)
print(x)
#A high standard deviation means that the values are spread out over a wider range.
sp1 = [32,111,138,28,59,77,97]
x = numpy.std(sp1)
print(x)
"""
To calculate the variance you have to do as follows:
1. Find the mean:
2. For each value: find the difference from the mean:
3. For each difference: find the square value:
4. The variance is the average number of these squared differences:
"""
variance_find = [32,111,138,28,59,77,97]
x = numpy.var(variance_find)
print(x)
# mean = 77.4
# difference from the mean: 32 - 77.4 = -45.4 and so on
# each difference: find the square value: (-45.4)2 = 2061.16
# The variance is the average number of these squared differences = 1432.2
#Standard Deviation is often represented by the symbol Sigma: σ

#What is the age that 75% of the people are younger than?
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)
#What is the age that 90% of the people are younger than?
x = numpy.percentile(ages, 90)
print(x)
#Data Distribution
#use the Python module Matplotlib to draw a histogram.
#Create an array containing 250 random floats between 0 and 5
x = numpy.random.uniform(0.0, 5.0, 250)
#print(x)
plt.hist(x, 5)
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#Normal Data Distribution
#A normal distribution graph is also known as the bell curve because of it's characteristic shape of a bell.
#x = numpy.random.normal(5.0, 1.0, 100000)
#plt.hist(x, 100)
#plt.show()
#A scatter plot is a diagram where each value in the data set is represented by a dot.
x_axis = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y_axis = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x_axis, y_axis)
plt.show()
x = numpy.random.normal(5.0, 1.0, 10)
print('\n')
print(x)
y = numpy.std(x)
print(y)

#Linear Regression uses the relationship between the data-points to draw a straight line through all them.
#The term regression is used when you try to find the relationship between variables.
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print('p=',p)
"""
slope : float Slope of the regression line. 
intercept : float Intercept of the regression line. 
rvalue : float The Pearson correlation coefficient(relationship). 
The square of ``rvalue`` is equal to the coefficient of determination. 
pvalue : float The p-value for a hypothesis test whose null hypothesis is that the slope is zero, 
using Wald Test with t-distribution of the test statistic. 
stderr : float Standard error of the estimated slope (gradient), 
under the assumption of residual normality. 
intercept_stderr : float Standard error of the estimated intercept, under the assumption of residual normality.
"""

#Polynomial regression, like linear regression,
# uses the relationship between the variables x and y
# to find the best way to draw a line through the data points.
x_axis_hour = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y_axis_speed = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel1 = numpy.poly1d(numpy.polyfit(x_axis_hour, y_axis_speed, 3))
myline1 = numpy.linspace(1,22,100)
plt.scatter(x_axis_hour, y_axis_speed)
plt.plot(myline1, mymodel1(myline1))
plt.show()
#The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
print(r2_score(y_axis_speed, mymodel1(x_axis_hour)))
#The result 0.94 shows that there is a very good relationship,
# and we can use polynomial regression in future predictions.

data_frame_object = pandas.read_csv("C:\\Users\MD Mojidul Islam\Downloads\data.csv")
x_df = data_frame_object[['Weight', 'Volume']]
y_df = data_frame_object['CO2']
#print(y_df)
regr = linear_model.LinearRegression()
regr.fit(x_df, y_df)
#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
#coefficient
print(regr.coef_)
"""
The result array represents the coefficient values of weight and volume.
Weight: 0.00755095
Volume: 0.00780526
We have predicted that a car with 1.3 liter engine, and a weight of 2300 to 3300 kg, 
will release approximately 115 grams of CO2 for every kilometer it drives.
Which shows that the coefficient of 0.00755095 is correct:
107.2087328 + (1000 * 0.00755095) = 114.75968
"""

#Scale Features
"""
standardization method for scaling uses this formula:
z = (x - u) / s
Where z is the new value, x is the original value, u is the mean and s is the standard deviation.
"""
print("standardization method for scaling")
df = pandas.read_csv("C:\\Users\MD Mojidul Islam\Downloads\data.csv")
X_df = df[['Weight', 'Volume']]
scaledX = scale.fit_transform(X_df)
print(scaledX)

#predict the CO2 emission from a car
#When the data set is scaled, you will have to use the scale when you predict values
df1 = pandas.read_csv("C:\\Users\MD Mojidul Islam\Downloads\data.csv")
X_df = df1[['Weight', 'Volume']]
Y_df = df1['CO2']
scaledX = scale.fit_transform(X_df)
regr = linear_model.LinearRegression()
regr.fit(scaledX, Y_df)
scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)


