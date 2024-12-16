import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,4,9,16,25]
#plt.plot(x,y)
plt.plot(x,y,color='red',linestyle='--',marker='o',markersize=9,linewidth=3)
plt.grid(True)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Basic Line Plot')
plt.show()

## Use multiple plots
z=[2,4,6,8,12]

plt.figure(figsize=(9,5))
#plt.subplot(1,2,1)
plt.subplot(2,2,1)
plt.plot(x,y,color='green')
plt.title('Plot 1')

#plt.subplot(1,2,2)
plt.subplot(2,2,2)
plt.plot(y,z,color='red')
plt.title('Plot 2')

plt.subplot(2,2,3)
plt.plot(x,z,color='blue')
plt.title('Plot 3')

plt.subplot(2,2,4)
plt.plot(y,z,color='yellow')
plt.title('Plot 4')

plt.show()

##Bar plots
categories=['A','B','C','D','E']
values = [5,7,3,6,8]
plt.bar(categories, values, color='green')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Basic Line Plot')

## Create a histogram
data = [1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5]
plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.show()

## create a scatter plot
x=[1,2,3,4,5,6]
y=[2,3,4,5,6,7]
plt.scatter(x,y, color='red',marker='x')
plt.show()

## create a pie chart
labels=['A','B','C','D']
sizes = [20,30,40,10]
colors=['gold','green','red','blue']
explode = (0.2,0,0,0)

plt.pie(sizes,labels=labels, colors=colors, autopct='%1.1f%%')
plt.show()



