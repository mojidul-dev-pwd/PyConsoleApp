# import sys
# write a comment line
# print("hello")
#C:\Users\MD Mojidul Islam\AppData\Local\Programs\Python\Python313\Scripts
#pip list
#pip install numpy
#pip install scipy
#pip install matplotlib
import mymodule as mx
import platform
import datetime
import math
import json
import re
import camelcase
"""
Hello multiline comment
Test multiline comment
"""
#from tkinter.scrolledtext import example

name = 'Mojidul Islam'
print(name)
# from math import cos, radians

# for i in range(360):
#     print(cos(radians(i)))

num1 = 20
num2 = 65
print(f"My name is {name} And total mark is { num1 + num2 }")

#multiline string
multilineVariable = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multilineVariable)
print('\n')
# multiline string usng '''
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Slicing a string
b = "Hello, World!"
print(b[1:5])
# Slice From the Start
print(b[:5])
# Slice To the End
print(b[3:])
print(b.upper())
print(b.lower())

#The strip() method removes any whitespace from the beginning or the end
cc = " Hello, World! "
print(cc.strip())
print(cc.replace("H","J"))
dd =cc.split(",")
print(dd[0])

# f format
age = 45
txt = f"My name is Mojidul, I am {age}"
print(txt)

# Display the price with 2 decimals
price = 59
prodPrice = f"The price is {price:.2f} dollars"
print(prodPrice)


#bytes is an immutable object
numList = [1,3,5,6,255,252] #Range 0 to 255
b = bytes(numList)
#b[1] = 3 not supported cause of immutable
print(type(b))

numList1 = [2,5,7,255,248]
b1 = bytearray(numList1)
b1[1] = 100
print(type(b1))

#None type
x = None
print(type(x))

#List declaration
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
fruitList = ["apple", "banana", "cherry"]
print(type(fruitList))
print(len(fruitList))
print(fruitList)

list1 = ["abc", 34, True, 40, "male"]

# Using the list() constructor to make a List
fruitList2 = list(("apple", "banana", "cherry"))
print(fruitList2)

# access a list
print('Access a list')
testlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(testlist[2:5])
#get from start to 4 elements
print(testlist[:4])
# start from position 3 to end
print(testlist[2:])
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
print(testlist[-4:-1])
if "apple" in testlist:
  print("Yes, 'apple' is in the fruits list")
print(testlist)
testlist[4] = "blackcurrant"
print(testlist)
# first index is start from(array) then last index upto this number of elements change by
testlist[1:3] = ["blackcurrant", "watermelon"]
print(testlist)
testlist.insert(2, "watermelon")
print(testlist)
testlist.append("orange")
print(testlist)
tropical = ["mango", "pineapple", "papaya"]
#add another list items
testlist.extend(tropical)
print(testlist)
#add tuples into list items
thistuple = ("kiwi", "Hang")
testlist.extend(thistuple)
print(testlist)
#remove specific item from lists(Remove the first occurrence)
testlist.remove("watermelon")
print(testlist)
#Remove the second item from a list
testlist.pop(1)
print(testlist)
#remove the last index from a list items
testlist.pop()
print(testlist)
#remove another way
del testlist[0]
print(testlist)
anotherlistRemove = ["apple", "banana", "cherry"]
del anotherlistRemove
#print(anotherlistRemove)
listTest2 = ["apple", "banana", "cherry"]
#after clear a list is empty now
listTest2.clear()
print('Length of this list :', len(listTest2))
numbers = [2, 3, 5, 2, 11, 2, 7]
# check the count of 2
count = numbers.count(2)
print('Count of 2:', count)
#loop
looplist = ["apple", "banana", "cherry"]
for x in looplist:
  print(x)
#loop through index
print('Loop through index')
for i in range(len(looplist)):
  print(looplist[i])
for i in range(3):
    print(i)
print('Using while loop')
i=0
while i < len(looplist):
    print(looplist[i])
    i = i+1
print('Looping Using List Comprehension')
[print(x) for x in looplist]
print('create a new list from existing list items apply condition')
fruits = ["apple", "kiwi", "banana", "cherry", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
print('another way to create a new list')
newlist11 = [x for x in fruits if "a" in x]
#newlist = [x for x in fruits if x != "apple"]
print(newlist11)
print('sorted list')
fruits.sort()
print(fruits)
print('sort with descending')
fruits.sort(reverse = True)
print(fruits)
fruits.reverse()
print(fruits)
print('copy a list')
mylist = fruits.copy()
print(mylist)
print('using list method to copy')
mylist2 = list(fruits)
print(mylist2)
print('using slice : operator to copy a list')
mylist3 = fruits[:]
print(mylist3)
print('using +, loop with append and extend() method we create a join list')
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
print('Tuple items are ordered, unchangeable, and allow duplicate values.')
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)
print(len(thistuple))
print(type(thistuple))
print('Access Tuple Items')
print(thistuple[1]) # start begin using index
print(thistuple[-1]) # start from last item
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
thistuple2 = ("apple", "banana", "cherry")
y = list(thistuple2)
y.append("orange")
thistuple2 = tuple(y)
print(thistuple2)
print('using del to delete the tuple')
deltuple = ("apple", "banana", "cherry")
print(len(deltuple))
del deltuple
#print(len(deltuple))
print('Unpacking a tuple')
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#Assign the rest of the values as a list called "red":
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#anohter way
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#how to add one more item in tuple
this_tuple = ("apple", "banana", "cherry")
y = ("orange",)
this_tuple += y
print(this_tuple)
#how to remove tuple item
y = list(this_tuple)
y.remove("apple")
this_tuple = tuple(y)
print(this_tuple)
#apply loop in a tuple
for x in this_tuple:
  print(x)
print('another way for loop')
for i in range(len(this_tuple)):
  print(this_tuple[i])
print('while loop')
wi=0
while wi<len(this_tuple):
    print(this_tuple[i])
    wi = wi + 1
print('tuple join')
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print('another way to join tuple')
tuple3 = tuple1 + tuple2
print(tuple3)
print('multiple tuple')
mutiple_tuple = this_tuple * 2
print(mutiple_tuple)
no_items_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = no_items_tuple.count(5)
print(x)
x = no_items_tuple.index(8)
print(x)
print('A set is a collection which is unordered, unchangeable*, and unindexed.')
example_set = {"Apple", "Banana", "Orange", "Guava"}
print(example_set)
print('Set items are unordered, unchangeable, and do not allow duplicate values.')
#not show error but remove itself duplication and consider True and 1 are same
thisset = {"apple", "banana", "cherry", "apple",True,1,2,False, 0}
print(thisset)
print(type(thisset))
# note the double round-brackets
thisset11 = set(("apple", "banana","orange", "cherry"))
print(thisset11)
for x in thisset11:
  print(x)
#return true or false
print("banana" in thisset11)
print("banana" not in thisset11)
thisset11.add("lemon")
print(thisset11)
tropical = {"pineapple", "mango", "papaya"}
thisset11.update(tropical)
print(thisset11)
#The object in the update() method does not have to be a set, it can be
# any iterable object (tuples, lists, dictionaries etc.).
mylist = ["kiwi", "orange"]
thisset11.update(mylist)
print(thisset11)
thisset11.remove("orange")
print(thisset11)
#Remove "banana" by using the discard() method
thisset11.discard("banana")
print(thisset11)
#If the item to remove does not exist, discard() will NOT raise an error.
#pop() methods remove random item and return this item
x = thisset11.pop()
print(x)
print(thisset11)
#clear() method empties the set
thisset11.clear()
print(thisset11)
#del keyword will delete the set completely
del thisset11
#print(thisset11)
print('using join method in set')
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print('using | operator method in set')
set4 = set1 | set2
print(set4)
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
print('you can join set and tuple')
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
#The  | operator only allows you to join sets with sets,
# and not with other data types like you can with the  union() method.
#Both union() and update() will exclude any duplicate items.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
#The & operator only allows you to join sets with sets,
# and not with other data types like you can with the intersection() method.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)
#The difference() method will return a new set that will contain only the items
# from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
#You can use the - operator instead of the difference() method, and you will get the same result.
#- operator only allows you to join sets with sets, and not with other
# data types like you can with the difference() method.
set3 = set1 - set2
print(set3)
#The difference_update() method will also keep the items from the first set that are not in the other set,
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
# ^ operator only allows you to join sets with sets
# The symmetric_difference_update() method will also keep all but the duplicates,
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
print("=============dictionary======================")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# duplicate not allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
thisdict = dict(name = "Mojidul", age = 41, country = "Bangladesh")
print(thisdict)
x = thisdict["name"]
print(x)
x = thisdict.get("country")
print(x)
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)
if "name" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
thisdict["name"] = 'Mojidul Islam'
x = thisdict.get("name")
print(x)
thisdict.update({"age": 45})
print(thisdict)
#add an item
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"color": "green"})
print(thisdict)
thisdict.pop("age")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["country"]
print(thisdict)
mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)
thisdict.clear()
print(thisdict)
del thisdict
#print(len(thisdict))
#nested loop
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

# conditional & if statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#Short Hand If
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")
if not a > b:
  print("a is NOT greater than b")
#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
a = 33
b = 200
if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Mojidul", "Islam")
#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Nayeem", lname = "Islam")
#Default Parameter Value
def my_function(country = "Bangladesh"):
  print("I am from " + country)
my_function("Soudi Arabia")
my_function()
def no_return_function():
  pass
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
  else:
    result = 0
  return result
res = tri_recursion(6)
print("Recursion Example Results:", res)
# lamda expression
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a,b,c:a+b+c
print(x(3,4,5))
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#Array
cars = ["Ford", "Volvo", "BMW"]
print(cars)
cars.append("Honda")
print(cars)
#remove the second value of array
cars.pop(1)
print(cars)
cars.remove("Ford") # if not found getting error
print(cars)
x = cars.count("BMW")
print(x)
cars.reverse()
print(cars)
cars.sort()
print(cars)
x = cars.index("Honda")
print('index of arrary',x)

#call another module
a11 = mx.person1["age"]
print(a11)
msg = mx.greeting("Mojidul Islam")
print(msg)
#built in module
x = platform.system()
print(x)
y = platform.processor()
print(y)
x = dir(platform)
print(x)
print("============ datetime ==============")
dt = datetime.datetime.now()
print(dt)
print(dt.year) #shows only year
print(dt.strftime("%A")) # shows only day name like friday
#create a date object
x = datetime.datetime(2020, 5, 17)
print(x)
ddmmyyyy = dt.strftime("%d-%m-%Y") #shows dd-mm-yyyy
print(ddmmyyyy)
hhmmss = dt.strftime("%H-%M-%S")
print(hhmmss)
hhmmssamorpm = dt.strftime("%I-%M-%S %p")
print(hhmmssamorpm)
local_version_date = dt.strftime("%x")
print(local_version_date)
local_vertion_time = dt.strftime("%X")
print(local_vertion_time)
microsecond = dt.strftime("%f")
print(microsecond)
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
x = abs(-7.25)
print(x)
x = pow(4, 3)
print(x)
sqrt = math.sqrt(4)
print(sqrt)
x = math.ceil(1.4)
z = math.floor(1.5)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1
print(z)
x = math.pi
print(x)
#Convert from JSON to Python
x = '{"name":"Mojidul","Country":"Bangladesh"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["Country"])
#Convert from Python to JSON
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON
y = json.dumps(x)
# the result is a JSON string:
print(y)
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, sort_keys=True))
#regular expression test
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
#findall method
x = re.findall("ai", txt)
print(x)
x = re.findall("Portugal", txt)
print(x)
#Split the string at every white-space character
x = re.split("\s", txt)
print(x)
#Split the string at the first white-space character
x = re.split("\s", txt, 1)
print(x)
#Replace all white-space characters with the digit "9"
x = re.sub("\s", "9", txt)
print(x)
x = re.sub("\s", "9", txt, 2)
print(x)
#Search for an upper case "S" character in the beginning of a word, and print its position
x = re.search(r"\bS\w+", txt)
print(x.span())
#Search for an upper case "S" character in the beginning of a word, and print the word
x = re.search(r"\bS\w+", txt)
print(x.group())
x = re.findall('[a-c]', txt)
print(x)
#after install --
#pip install camelcase
#pip uninstall camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
#try catch block
try:
  print(xx)
except NameError:
  print("Variable xx is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(xx)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
