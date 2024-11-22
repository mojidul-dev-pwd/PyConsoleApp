import sys
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#Train/Test
"""
Train/Test is a method to measure the accuracy of your model.
80% for training, and 20% for testing.
Train the model means create the model.
Test the model means test the accuracy of the model.
"""
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

#for train 80% of the model
plt.scatter(train_x, train_y, color="red")
plt.show()

#for test 20% of the model
plt.scatter(test_x, test_y)
plt.show()

#all
#plt.scatter(x, y)
#plt.show()

#polynomial regression
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
r2 = r2_score(train_y, mymodel(train_x))
print('')
print('training r2 = ',r2)
testing_r2 = r2_score(test_y, mymodel(test_x))
print('testing r2 = ',testing_r2)
"""
The result 0.809 shows that the model fits the testing set as well, 
and we are confident that we can use the model to predict future values.
"""

#How much money will a buying customer spend,
# if she or he stays in the shop for 5 minutes?
print(mymodel(5))
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

