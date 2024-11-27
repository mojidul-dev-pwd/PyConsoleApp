import sys
import datetime
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