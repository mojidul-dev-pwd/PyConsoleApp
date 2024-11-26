import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")


a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))


lhs = a**2 + b**2
rhs = c**2         #

if lhs == rhs:
    print(f"{a}² + {b}² = {c}² holds true.")
else:
    print(f"{a}² + {b}² ≠ {c}².")

