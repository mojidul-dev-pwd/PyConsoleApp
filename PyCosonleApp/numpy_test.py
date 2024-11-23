import numpy as np

#one dimensional array
test_array = np.array([1,2,3,4,5,6])
print(test_array)
test_arr_tuple = np.array((1,2,3,4))
print(test_arr_tuple)

two_dimensional_array = np.array([[1,2,3,4],[5,6,7,8]])
print(two_dimensional_array)
print('Three Dimensional array')
three_dimensional_array = np.array([[[1,2,3],[5,6,7]],[[3,6,9],[4,6,8]]])
print(three_dimensional_array)

#Check how many dimensions the arrays have
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Create an array with 5 dimensions and verify that it has 5 dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

#Access the element from an array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# First row=>Second Column=>Third element
print(arr[0, 1, 2])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

"""
Array slicing
[start:end]
[start:end:step]
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
#index 4 to the end
print(arr[4:])
#beginning to index 4
print(arr[:4])
#Negative Slicing
#Slice from the index 3 from the end to index 1 from the end
print(arr[-3:-1])
#Use the step value to determine the step of the slicing(recurring)
arr = np.array([1, 2, 3, 4, 5, 6, 7,8,9,10,11,12])
print(arr[1:12])
print(arr[1:12:3])
print(arr[1:12:4])
#Return every other element from the entire array:
print(arr[::2])
#From the second element, slice elements from index 1 to index 4 (not included)
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
#From both elements, return index 2
print(arr[0:2, 2])
print(arr[0:2, 3])
#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print(arr[0:2, 1:4])

#numpy data types
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
#array copy
print('array copy')
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
#Make a view, change the original array, and display both arrays should be same
# Even change into view object
x = arr.view()
arr[0] = 42
x[1] = 32
print(arr)
print(x)
#Print the value of the base attribute to check if an array owns it's data or not
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
#shape that returns a tuple with each index having the number of corresponding elements
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [2, 6, 4, 8]])
print(arr.shape)
# reshape Convert the following 1-D array with 12 elements into a 2-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# general way to display
for x in arr:
  for y in x:
    for z in y:
      print(z)
# dynamic way to display
for x in np.nditer(arr):
  print(x)

#Enumerate on following 2D array's elements
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

#Joining array using concatenate
print('join array')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
#Joining array using Stack
print('join array using Stack')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2))
print(arr)
#using hstack()
print('join array using hstack')
arr = np.hstack((arr1, arr2))
print(arr)
#using vstack()
print('join array using vstack')
arr = np.vstack((arr1, arr2))
print(arr)
#using dstack()
print('join array using dstack')
arr = np.dstack((arr1, arr2))
print(arr)
#Join two 2-D arrays along rows (axis=1)
print('join 2-D array')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#Split the array in 3 parts
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
newarr = np.array_split(arr, 4)
print(newarr)
print('Split the 2-D array into three 2-D arrays')
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
#We can also use hsplit() and vsplit() for spling

print('Find the indexes where the values are even')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)
print('Find the indexes where the values are odd')
x = np.where(arr%2 == 1)
print(x)

print('Find the indexes where the value 7 should be inserted')
x = np.searchsorted(arr, 7)
print(x)
print('Find the indexes where the value 7 should be inserted, starting from the right')
arr = np.array([6, 7, 8, 9])
index_from_right = np.searchsorted(arr, 7, side='right')
print(index_from_right)
print('Find the indexes where the values 2, 4, and 6 should be inserted')
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

print('array sort')
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

print('array filter')
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

print('random')
ran_array = np.random.randint(1,50,10)
print(ran_array)
print('range')
arr = np.arange(25)
print(arr)
print('reshape')
new_array = arr.reshape(5,5)
print(new_array)





