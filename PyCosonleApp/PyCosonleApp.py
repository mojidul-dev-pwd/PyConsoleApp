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



