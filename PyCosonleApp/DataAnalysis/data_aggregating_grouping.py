import pandas as pd

data= pd.read_csv("../files/data_sample.csv")
df = pd.DataFrame(data)
print(df.head(5))
print(df.dtypes)

data_group_single = df.groupby('City')['Profit'].mean()
print(data_group_single)

data_group_multiple = df.groupby(['City','Category'])['Discount'].sum()
print(data_group_multiple)

data_group_multiple1 = df.groupby(['City','Category'])['Discount'].mean()
print(data_group_multiple1)

##Aggregate multiple functions
print("Multiple functionality")
data_multiple_functionality = df.groupby('City')['Profit'].agg(['mean','sum','count'])
print(data_multiple_functionality)

##Marging and joining dataframes
df1= pd.DataFrame({'Key':['A','B','C'],'Value1':[1,2,3]})
df2= pd.DataFrame({'Key':['A','B','D'],'Value2':[4,5,6]})

df3 = pd.merge(df1,df2)
print(df3)
## OR
df3 = pd.merge(df1,df2, on="Key", how="inner")
print(df3)
df3 = pd.merge(df1,df2, on="Key", how="outer")
print(df3)
df3 = pd.merge(df1,df2, on="Key", how="left")
print(df3)

