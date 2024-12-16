import numpy as np
from scipy.spatial.distance import pdist

#two-dimensional array
arr1 = np.array(([1,2,3,4,5],[2,3,7,5,6]))
##shape means two rows and five column
print(arr1.shape)
print("Dimension = ", arr1.ndim)

print(np.arange(0,10,2))
##shows two-dimensional array
print(np.arange(0,10,2).reshape(5,1))
#three column and four column
print(np.ones((3,4)))
##identity matrix
print(np.eye(3))

##vectorised operation
arr2= np.array([1,2,3,4,5])
arr3 = np.array([21,22,34,45,67])
#element wise addition
print("Addition", arr2+arr3)
#element wise substruction
print("substruction", arr3-arr2)
#element wise multiplication
print("multiplication", arr3*arr2)
#element wise divided
print("divided", arr3/arr2)

##universal function
arr4=np.array([2,3,4,5,6])
print(np.sqrt(arr4))
#exponential
print(np.exp(arr4))
print(np.sign(arr4))
print(np.log(arr4))

##array slicing and indexing
arr5=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#second row start to last row and third column start to last all row
print(arr5[1:,2:])
#first row start upto third row and third column start to last all row
print(arr5[0:2,2:])
#second row start to last row and second column and fourth column of second and third row
print(arr5[1:,1:3])

#statistical concept normalization
data = np.array([1,3,5,6,3,8])
mean = np.mean(data)
standard_deviation= np.std(data)
normalized_data= (data-mean)/standard_deviation
print("normalized data", normalized_data)

median = np.median(data)
print("Median", median)

variance = np.var(data)
print("variance", variance)

print(data>4)

## start with panda
import pandas as pd
data1 = [1,2,3,4,5,6]
series = pd.Series(data1)
print("Series", series)
data2 = {'a':1,'b':2,'c':3}
dic_series = pd.Series(data2)
print(dic_series)

data4 = [10,20,30]
index= ['a','b','c']
pd_series = pd.Series(data4, index=index)
print(pd_series)

#DataFrame
#Create a dataframe using dictionary
data_for_dataframe= {
    "Name":["Mojidul","Nayeem","Sarmin","Fatima-Tuz-zuhra"],
    "Age":[40,14,35,5],
    "City":["Kurigram","Dhaka","Rangpur","Dhaka"]
}
df = pd.DataFrame(data_for_dataframe)
print(type(df))
print(df)

data11= pd.read_csv("../files/USA_Housing.csv")
df2 = pd.DataFrame(data11)
#top 5 records
print(df2.head(5))
#last 5 records
print("Last five rows")
print(df2.tail(5))
print(df2.describe())
print(df2.isnull())
print(df2.isnull().sum())
##filling missing value by o
df2.fillna(0)
##create a new column with fill value
df2['new_column']= df2['Price'].fillna(df2['Price'].mean())
print("+++++++++++++==========")
df2 = df2.rename(columns={'new_column':'column_renamed'})
print(df2)
##change data types
print(df2.dtypes)
df2['column_renamed'] = df2['column_renamed'].fillna(df2['column_renamed'].mean()).astype(int)
print(df2)
df2['new_column2']=df2['Avg. Area Income'].apply(lambda x:x*2)
print(df2)
print(df2.columns)
print(df2.loc[0][0])
print(df2.iloc[0][1])
print(df2.at[0,'Address'])
#Column drop if you need row drop set axis=0
#if you need permanent delete set inplace=True
#print(df2.drop("Address", axis=1, inplace=True))
print(df2.drop("Address", axis=1))
print(df2)



