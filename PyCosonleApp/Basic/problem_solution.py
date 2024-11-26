import sys
import datetime
from math import pi
import calendar
from datetime import date

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

r = float(input("Input the radius of the circle : "))
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









