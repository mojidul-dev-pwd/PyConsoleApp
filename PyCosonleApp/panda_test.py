import numpy as np
import pandas as pd
from numpy.matlib import randn

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
dic = {'a':10,'b':20,'c':30}

res = pd.Series(data = my_data)
print(res)

res = pd.Series(data = my_data, index=labels)
print(res)

ses1 = pd.Series([1,2,3,4],['Bangladesh','India','USA','Soudi Arabia'])
print(ses1)
print(ses1['USA'])

#DataFrame
data_frame = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(data_frame)
print(data_frame['W'])
print(data_frame[['W','X']])
data_frame['new'] = data_frame['W']+data_frame['X']
print(data_frame)

dd = data_frame.drop('new', axis=1)
print(dd)

dd1 = data_frame.loc[['A','B'],['W','Y']]
print(dd1)

comp = data_frame > 0
print(comp)

comp_specific = data_frame['W'] > 0
print(comp_specific)

result_df = data_frame[data_frame['W'] > 0]
print(result_df)

#index levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df = pd.DataFrame(randn(6,2),hier_index, ['A','B'])
print(df)
print(df.loc['G1'])
print(df.loc['G1'].loc[1])
print('Cross section')
print(df.xs('G1'))

data = {
    'Company':['Google','Google','DIU','DIU','SELISE','SELISE'],
    'Person':['Sibli','Sibli Bro','Mostofa Jaman','Sharmin Jahan','Mojidul','Sayem'],
    'Sales':[200,120,340,124,243,350]
}
df = pd.DataFrame(data)
print(df)
gb_df = df.groupby('Company')
sum = gb_df.sum()
print(sum)
single = gb_df.sum().loc['SELISE']
print(single)
count = df.groupby('Company').count()
print(count)
# similarly use min, max etc
desc = df.groupby('Company').describe().transpose()
print(desc)
"""
avg = gb_df.mean()
print(avg)
std = gb_df.std()
print(std)
"""

df1 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
},
index = [0,1,2,3])

df2 = pd.DataFrame({
    'A':['A4','A5','A6','A7'],
    'B':['B4','B5','B6','B7'],
    'C':['C4','C5','C6','C7'],
    'D':['D4','D5','D6','D7']
},
index = [4,5,6,7])

df3 = pd.DataFrame({
    'A':['A8','A9','A10','A11'],
    'B':['B8','B9','B10','B11'],
    'C':['C8','C9','C10','C11'],
    'D':['D8','D9','D10','D11']
},
index = [8,9,10,11])

df_concat = pd.concat([df1,df2,df3])
print(df_concat)

df_concat = pd.concat([df1,df2,df3], axis=1)
print(df_concat)
#left is an df
#right is an df
#pd.merge(left,right,how='inner',on='key')

df = pd.DataFrame(
    {
        'Col1':[1,2,3,4],
        'Col2':[444,555,666,444],
        'Col3':['abc','def','ghi','xyz']
    }
)
df.head()
print(df)
unique_df = df['Col2'].unique()
print(unique_df)
len_df = len(df['Col2'].unique())
print(len_df)
#shows same count
len_df = df['Col2'].nunique()
print(len_df)
value_wise_len_df = df['Col2'].value_counts()
print(value_wise_len_df)



