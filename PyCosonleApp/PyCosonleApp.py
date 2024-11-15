# import sys
# write a comment line
# print("hello")

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