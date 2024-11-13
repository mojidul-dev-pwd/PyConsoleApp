# import sys
# write a comment line
# print("hello")

"""
Hello multiline comment
Test multiline comment
"""
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
