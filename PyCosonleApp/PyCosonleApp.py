import sys
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

