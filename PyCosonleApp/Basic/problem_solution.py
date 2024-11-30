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
import string

#sum of 1 to 100 numbers
num = 100
sum1 = 0

for i in range(num+1):
    sum1 += i
print(sum1)

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
"""
r = float(input("Input the radius of the circle : "))
"""
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
f_extents = filename.split(".")
print(f_extents)

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
    res11 = ''
    for element in lst:
        res11 += str(element)
    return res11

print(str_concat_test([1, 5, 12, 2]))

name, age = "Mojidul Islam", 45
address = "Dhaka, Bangladesh"
print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

def sum_conditional(x1, y1):
    ism = x1 + y1
    if ism in range(15,20):
        return 20
    else:
        return ism
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

def sum2():
   print(1888888888888888888 + 266666666666666666666666)
cProfile.run('sum2()')

print(getpass.getuser())

local_hostname = socket.gethostname()
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]
first_ip = filtered_ips[:1]
print(first_ip[0])

def sum_digit_number(num1):
    x2 = num1 // 1000
    x1 = (num1 - x2 * 1000) // 100
    x2 = (num1 - x2 * 1000 - x1 * 100) // 10
    x3 = num1 - x2 * 1000 - x1 * 100 - x2 * 10
    return x2 + x1 + x2 + x3
print(sum_digit_number(5245))
#To sort three integers without using conditional statements and loops.
x,y,z = 10,3,15
min1 = min(x, y, z)
max1 = max(x, y, z)
middle = (x+y+z) - min1 - max1
print(min1, middle, max1)

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
result = list(filter(lambda x3: (x3 % 15 == 0), num_list))
print("Numbers divisible by 15 are", result)

# wildcard patterns using glob
file_list = glob.glob('*.*')
print(file_list)

nums_list = [34, 1, 0, -23, 12, -88]
positive_nums = list(filter(lambda x4: x4 > 0, nums_list))
print(positive_nums)

#multiple all element in an array
nums = [10, 20, 30]
mul = reduce(lambda x5, y5: x5 * y5, nums)
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

data = {'Fatima': 1, 'Nayeem': 2, 'Mojidul': 3}
json_string = json.dumps(data)
print(json_string)

print(format(10, '08b'))

#check the sum of three elements (each from an array) from three arrays is equal to a
# target value. Print all those three-element combinations.

import itertools
from functools import partial

# Define three lists and a target sum value.
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

def check_sum_array(cap_n, *num_arr):
    if sum(x6 for x6 in num_arr) == cap_n:
        return True, num_arr
    else:
        return False, num_arr

# Generate the Cartesian product of the three lists.
pro = itertools.product(X, Y, Z)

# Create a partial function using the 'check_sum_array' function and the target sum 'T'.
func = partial(check_sum_array, T)

# Use 'starmap' to apply the partial function to each element in the Cartesian product.
sums = list(itertools.starmap(func, pro))

# Use a set to store unique valid combinations.
result = set()

# Iterate through the sums and print unique valid combinations.
for s in sums:
    if s[0] == True and s[1] not in result:
        result.add(s[1])
        print(result)

# permutation theory P(6,2) = Factorial(6) / Factorial(6-2) = 30
# combination theory C(6,2) = Factorial(6) / Factorial(2) * Factorial(6-2) = 15

# List to permute
data = [1, 2, 3]
string_maps = {"abc","def","ghi","jkl","mno","pqrs", "tuv","wxy","z" }
result_perms = []
result_com = []

# Generate all permutations
permutations = itertools.permutations(data)
combinations = itertools.combinations(string_maps, 2)

# Print permutations
for perm in permutations:
    result_perms.append(perm)
print("Permutation Result")
print(result_perms)

# Print Combinations
for com in combinations:
    result_com.append(com)
print("Combinations Result")
print(result_com)

def is_palindrome(n):
    print(str(n)[::-1])
    return str(n) == str(n)[::-1]

# Test cases
print(is_palindrome(100))    # False
print(is_palindrome(252))    # True

#Remove Duplicates from Array
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr = list(set(arr))
print(unique_arr)

def find_median(num_arr):
    nums.sort()
    n = len(num_arr)
    # Calculate the middle index
    m_index = n // 2
    if n % 2 == 0:
        return (num_arr[m_index-1]+ num_arr[m_index])/2
    else:
        return num_arr[m_index]
print(find_median([1,2,3,4,5]))
print(find_median([1,2,3,6,4,5]))

def count_negative_positive_num(num_arr):
    if not num_arr:
        return []
    return [len([x11 for x11 in num_arr if x11 < 0]), len([x12 for x12 in num_arr if x12 > 0])]
print("Result of Negative and Positive Count = ", count_negative_positive_num( [1, 2, 3, -4, -5]))

def is_valid_emp_code(emp_code):
    # digit must be 8 or 12
    #return len(emp_code) in [8, 12] and emp_code.isdigit()
    # digit between 8 or 20
    return emp_code.isdigit() and 8 <= len(emp_code) <= 20

print(is_valid_emp_code('123456783'))

def sum_smallest_three_num(num_arr):
    return sum(sorted(num_arr)[:3])
print("Sum Smallest three numbers = ",sum_smallest_three_num([10, 20, 30, 40, 50, 60, 7]))

def mask_by_char(string_data):
    print('*' * (len(string_data) - 5))
    return '*' * (len(string_data) - 5) + string_data[-5:]
print(mask_by_char("kdi39323swe"))

def nums_cumulative_sum(nums_list1):
    return [sum(nums_list1[:i1 + 1]) for i1 in range(len(nums_list1))]
print(nums_cumulative_sum([10, 20, 30, 40, 50, 60, 7]))

def adjacent_num_product(list_nums):
    return max(a * b for a, b in zip(list_nums, list_nums[1:]))
print("Multiple max two number = ",adjacent_num_product([1, 2, 3, 4, 5, 6]))

def odd_even_position_with_index(num_arr):
    return all(num_arr[i2] % 2 == i2 % 2 for i2 in range(len(num_arr)))
print("Odd Even with position same odd or even ",odd_even_position_with_index([2, 1, 4, 3, 6, 7, 6, 3]))
print("Odd Even with position same odd or even ",odd_even_position_with_index([2, 1, 4, 3, 6, 7, 6, 4]))

def is_narcissistic_num(num_arr):
    return num_arr == sum([int(x) ** len(str(num_arr)) for x in str(num_arr)])
print(is_narcissistic_num(153))
print(is_narcissistic_num(1634))

#same type increment return true
def highest_lowest_num(str_1):
    num_list_1 = list(map(int, str_1.split()))
    return max(num_list_1), min(num_list_1)
print("Highest and lowest number ",highest_lowest_num("1 4 5 77 9 0"))

def increasing_trend(num_arr):
    if (sorted(num_arr) == num_arr):
        return True
    else:
        return False
print(increasing_trend([1,2,3,4]))
print(increasing_trend([-4,-3,-2,-1]))
print(increasing_trend([-1,-2,-3,-4]))
print(increasing_trend([2,4,6,8]))

def sum_index_multiplier(num_arr):
    print(enumerate(num_arr))
    return sum(j * i for i, j in enumerate(num_arr))
print(sum_index_multiplier([1,2,3,4]))
print(sum_index_multiplier([3]))

def oldest_student(students):
    return max(students, key=students.get)
print(oldest_student({"Mahi Sarkar": 12, "Ruhul Amin": 11,
                      "Sara Jaker": 14, "Bodrul Islam": 11,
                      "Nayeem Islam": 13}))

def digit_distance_nums(num1: int, num2: int) -> int:
    return sum(abs(i - j) for i, j in zip(map(int, str(num1)), map(int, str(num2))))
print(digit_distance_nums(509, 510))

for lower_letter in string.ascii_lowercase:
    print(lower_letter, end=" ")
print()
for upper_letter in string.ascii_uppercase:
    print(upper_letter, end=" ")
print()
print("Generate num array and string array using range from 1 to 10")
nums = range(1, 10)
print(list(nums))
print(list(map(str, nums)))

def is_not_prime(num_digit):
    res = False
    if num_digit > 1:
        #print((num_digit//2))
        # for i in range(2, (num_digit//2) + 1):
        #print(int(math.sqrt(num_digit)))
        for i in range(2, int(math.sqrt(num_digit)) + 1):
            if (num_digit % i) == 0:
                res = True
                #print("not prime")
                break
            else:
                res = False
                #print("prime")
        return res
    else:
        return res
#print(is_not_prime(4))
#print(is_not_prime(5))
#print(is_not_prime(12))
for x in filter(is_not_prime, range(1, 101)):
    print(x)

# Find a number that is maximum in its column and minimum in its row.
def matrix_number(matrix):
    result_1 = set(map(min, matrix)) & set(map(max, zip(*matrix)))
    return list(result_1)
print(matrix_number([[1,2], [2,3]]))
print(matrix_number([[1,2,3], [3,4,5]]))
print(matrix_number([[7,5,6], [3,4,4], [6,5,7]]))
print(set(map(min, [[1,2], [2,3]])))
print(set(map(max, zip(*([[1,2], [2,3]])))))

def is_pan_digital_num(n):
    return len(set(str(n))) == 10
print("Is pan digital?", is_pan_digital_num(1223334444555556666667777777888888889999999990))
print("Is pan digital?", is_pan_digital_num(1023456897))
print(is_pan_digital_num(102345679))

def oddish_evenish_num(n):
    print(sum(map(int, str(n))))
    return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'
print(oddish_evenish_num(120))
print(oddish_evenish_num(321))

def unique_nums(nums_1):
    return [i for i in nums_1 if nums_1.count(i) == 1]
print(unique_nums([1,2,3,2,3,4,5]))

def check_last_digit(x, y, z):
    print(str(x + z)[-1])
    print(str(y)[-1])
    return str(x + z)[-1] == str(y)[-1]
print(check_last_digit(12, 26, 44))
print(check_last_digit(145, 129, 104))