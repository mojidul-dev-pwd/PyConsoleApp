import sqlite3
##Connect database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

"""
cursor.execute('''
Create Table If Not Exists employee(
    id integer Primary Key,
    name Text Not Null,
    age Integer,
    department Text
)
''')
"""

##insert data
"""
cursor.execute('''
Insert into employee(name,age,department)
values('Mojidiul',40,'CSE')
''')

cursor.execute('''
Insert into employee(name,age,department)
values('Nayeem',13,'Army')
''')

cursor.execute('''
Update employee
Set name = 'Sharmin Jahan',
age = 35
Where id = 4
''')

cursor.execute('''
Delete from employee
Where id = 5
''')
##commit the change
connection.commit()
"""

cursor.execute('''
Select * from employee
''')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
Create Table If Not Exists sales_data(
    id integer Primary Key,
    date Text Not Null,
    product Text Not Null,
    region Text
)
'''
)
##Bulk insert
sales_data = [
    ('2023-01-01','Product1','Dhaka'),
    ('2023-02-01','Product2','Dhaka'),
    ('2023-03-01','Product1','Kurigram'),
    ('2023-04-01','Product2','Kurigram'),
    ('2023-05-01','Product1','Dhaka')
]

cursor.executemany('''
Insert into sales_data(date,product,region)
values(?,?,?)
''',sales_data)
##commit the change
connection.commit()

cursor.execute('''
Select * from sales_data
''')
row1s = cursor.fetchall()
for row in row1s:
    print(row)
connection.close()