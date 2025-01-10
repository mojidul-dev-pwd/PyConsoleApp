import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
mean = np.mean(speed)
print("Average value = ", mean)
median = np.median(speed)
print("Mid point value = ", median)
mode = stats.mode(speed)
print("Most common value = ", mode)

## How to calculate Standard deviation
"""
i) Find out Mean value
ii) ((i)-First pointer)**2+....+((i)-Last pointer)**2)
iii) ii)/No of pointer
iv) square root of (iii) -- This is standard deviation

A low standard deviation means that most of the numbers are close to the mean (average) value.
A high standard deviation means that the values are spread out over a wider range.
"""
speed1 = [86,87,88,86,87,85,86]
std = np.std(speed1)
print("Standard deviation = ", std)

## How to calculate percentile
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
percentile = np.percentile(ages, 75) ## Here 75 is a variable
print("Percentile ", percentile)

## Data Distributions
data_set = np.random.uniform(0.0, 5.0, 100000)
#plt.hist(data_set)
plt.hist(data_set, 100)
#plt.show()

## Normal Data Distributions or Gaussian Data Distribution
data_set1 = np.random.normal(5.0, 1.0, 100000)
plt.hist(data_set1, 100)
#plt.show()

## A scatter plot is a diagram where each value in the data set is represented by a dot.

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
#plt.show()

## Linear regression
## y = mx+c

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

mymodel = list(map(myfunc, x1))
print(mymodel)
## shows existing data
plt.scatter(x1, y1)
## Draw a linear regression line
plt.plot(x1, mymodel)
# shows figure
plt.show()








