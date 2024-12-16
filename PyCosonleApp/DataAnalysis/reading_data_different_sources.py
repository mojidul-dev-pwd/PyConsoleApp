import pandas as pd
from io import StringIO

data = '{"employeee_name": "Mojidul", "email":"mojidul31@gmail.com","job_profile":[{"title1":"Technical Lead","title2":"Staff Software Engineer","Salary":110000}]}'
rd = pd.read_json(StringIO(data))
print(rd)
print(rd.to_json())
print(rd.to_json(orient='index'))
print(rd.to_json(orient='records'))
#df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
#print(df.head(5))
#df.to_csv("wine.csv")

##data getting from html file
url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
#df11=pd.read_html(url)
#print(df11)

## another way
url1="https://en.wikipedia.org/wiki/Mobile_country_code"
df12 = pd.read_html(url1, match="Country",header=0)[0]
print(df12)

##reading from excel
df13 = pd.read_excel("test.xlsx")
print(df13)

##convert to pickle file
#df13.to_pickle('test_pickle')
df14 = pd.read_pickle('test_pickle')
print(df14)
