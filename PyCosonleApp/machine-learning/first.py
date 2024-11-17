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


