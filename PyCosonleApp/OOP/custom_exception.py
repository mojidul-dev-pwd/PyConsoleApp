
class Error(Exception):
    pass

class DobException(Error):
    pass

year = int(input("Please enter your dpb"))
age = 2024-year

try:
    if 30 >= age >= 20:
        print("The age is valid")
    else:
        raise DobException

except DobException:
    print("Sorry, Your age should be greater than 20 or less than 30")
