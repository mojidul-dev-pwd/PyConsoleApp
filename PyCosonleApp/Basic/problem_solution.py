import sys
import datetime
from functools import reduce
from math import pi
import calendar
from datetime import date
import math
import struct
import platform
import os
import multiprocessing
import cProfile
import getpass
import socket
import time
import glob
import json

#sum of 1 to 100 numbers
num = 100
sum = 0

for i in range(num+1):
    sum += i
print(sum)

#odd number from 1 to 100
o=[]
for i in range(num+1):
    if i%2 != 0:
        o.append(i)
print(o)

#even number from 1 to 100
e=[]
for i in range(num+1):
    if i != 0 and i%2 == 0:
        e.append(i)
print(e)

#string format
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
print(sys.version)
print(sys.version_info)

now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
exam_st_date = (11, 12, 2014)
print("date : %i / %i / %i" % exam_st_date)

r = 1.1
#r = float(input("Input the radius of the circle : "))
area = pi * r ** 2
print("The area of the circle with radius " + str(r) + " is: " + str(area))

def reverse(sentence):
    res = ""
    for word in sentence.split(" "):
        res = word + " " + res
    return res

# call reverse function
rev = "How are you"
print(reverse(rev))
# reverse a word
#repaper is a palindrome word
wrd = "Never odd or even"
print(wrd[::-1])

def is_palindrome(word):
    new_word = word[::-1]
    if word == new_word:
        return True
    else:
        return False

#call the palindrome function
print(is_palindrome("repaper"))

filename = "test.java"
f_extns = filename.split(".")
print(f_extns)

color_list = ["Red", "Green", "White", "Black"]
#print first and last color
print("%s %s" % (color_list[0], color_list[-1]))
#specific month calendar
print(calendar.month(2024,11))

# Define a start date as July 2, 2014
f_date = date(2014, 7, 2)
# Define an end date as July 11, 2014
l_date = date(2014, 7, 11)
# Calculate the difference between the end date and start date
delta = l_date - f_date
# Print the number of days in the time difference
print(delta.days)

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(is_vowel('c'))
print(is_vowel('a'))

def is_contain_member(member_data, n):
    for value in member_data:
        if n == value:
            return True
    return False
print('yes', is_contain_member([1, 5, 8, 3], 3))
print(is_contain_member([5, 8, 3], -1))

def histogram(items):
    for n in items:
        output = ""
        times = n
        while times>0:
            output += "*"
            times -=1
        print(output)

histogram([2, 3, 6, 5])

def str_concat_test(lst):
    result = ''
    for element in lst:
        result += str(element)
    return result

print(str_concat_test([1, 5, 12, 2]))

name, age = "Mojidul Islam", 45
address = "Dhaka, Bangladesh"
print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

def sum_conditional(x,y):
    isum = x+y
    if isum in range(15,20):
        return 20
    else:
        return isum
print(sum_conditional(10, 6))
print(sum_conditional(10, 12))

def add_two_integer(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be integers!"
    return a+b
print(add_two_integer('5', 6))
print(add_two_integer(10, 20))

#compound interest formula
# I = P(1+r)**n
def compound_interest(principal_amt, interest_rate, years):
    total_interest = principal_amt * ((1 + (0.01 * interest_rate)) ** years)
    return total_interest
print(compound_interest(10000, 3.5, 7))

# Calculate the distance between the two points using the distance formula.
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
print(distance)

#Python shell is executing in 32bit or 64bit mode on OS.
print(struct.calcsize("P") * 8)
#or
architecture = platform.architecture()
print(architecture)
print(architecture[0])
print("Name of the operating system:", os.name)
print("Name of the OS system:", platform.system())
print("Version of the operating system:", platform.release())

print("Current File Name: ", os.path.realpath(__file__))

cpu_count = multiprocessing.cpu_count()
print(cpu_count)

def sum():
   print(1888888888888888888 + 266666666666666666666666)
cProfile.run('sum()')

print(getpass.getuser())

local_hostname = socket.gethostname()
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]
first_ip = filtered_ips[:1]
print(first_ip[0])

def sum_digit_number(num):
    x = num // 1000
    x1 = (num - x * 1000) // 100
    x2 = (num - x * 1000 - x1 * 100) // 10
    x3 = num - x * 1000 - x1 * 100 - x2 * 10
    return x + x1 + x2 + x3
print(sum_digit_number(5245))
#To sort three integers without using conditional statements and loops.
x,y,z = 10,3,15
min = min(x,y,z)
max = max(x,y,z)
middle = (x+y+z)-min-max
print(min,middle,max)

print(sys.copyright)

print(sys.getrecursionlimit())

list_of_colors = ['Red', 'White', 'Black']
colors = '-'.join(list_of_colors)
print(colors)

num = [2, 3, 4, 5]
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
#ASCII Value
print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('@'))

file_size = os.path.getsize("../files/USA_Housing.csv")
print(file_size,"Bytes")
#custom display
x = 30
y = 20
print("%d+%d=%d" % (x, y, x+y))

print(time.ctime())

num_list = [45, 55, 60, 37, 100, 105, 220]

# Use an anonymous lambda function with the filter function to filter
# numbers in the list that are divisible by 15.
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are", result)

# wildcard patterns using glob
file_list = glob.glob('*.*')
print(file_list)

nums_list = [34, 1, 0, -23, 12, -88]
positive_nums = list(filter(lambda x: x>0, nums_list))
print(positive_nums)

#multiple all element in an array
nums = [10, 20, 30]
mul = reduce(lambda x,y: x*y, nums)
print(mul)

#memory location
str1 = "Python"
str2 = "Python"
print("Memory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))

order_amt = 212.37465
print('The total order amount comes to %.2f' % order_amt)
print('The total order amount comes to %.3f' % order_amt)

str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))

str1 = '122.22'
print("Original String: ", str1)
print("Added trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("Added leading zeros:")
str1 = '122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)

data = {'Alex': 1, 'Suresh': 2, 'Agnessa': 3}
json_string = json.dumps(data)
print(json_string)

print(format(10, '08b'))