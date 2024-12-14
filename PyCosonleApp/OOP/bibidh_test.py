my_list = [1,2,3,4,5]

iterator = iter(my_list)

try:
    print(next(iterator))
    #print(iterator.__next__())
except StopIteration:
    print("Your list has printed last element")

#generator
def cus_square(n):
    for i in range(3):
        yield i**2

a = cus_square(3)
print(next(a))
print(next(a))
print(next(a))

## Generator basically usages for large files reading
def read_large_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line

file_path= '../demofile.txt'

for line in read_large_file(file_path):
    print(line.strip())

##function copy
def welcome():
    return "Welcome greeting function."
#copy function
welcome()
wel = welcome
print("1",wel())
del welcome
print("2",wel())

#closures
#functions inside a function
def main_methods(msg):
    def sub_methods():
        print("This is sub methods")
        print(msg)
    return sub_methods()

main_methods("Welcome everyone")

##decorator
def main_methods_deco(func):
    def sub_methods():
        print("This is sub methods")
        func()
        print("This is end of sub methods")
    return sub_methods()

##assign decorator
@main_methods_deco
def introduce_methods():
    print("Welcome everyone to learn decorator")

##Another way of decorator
def my_decorator(func):
    def wrapper():
        print("This is sub methods")
        func()
        print("This is end of sub methods")
    return wrapper

@my_decorator
def say_hi():
    print("Hello !!!!!!!")

say_hi()

##Decorator with arguments
def repeat(n):
    def my_deco(func):
        def wrapper(*args, **kwagrs):
            for _ in range(n):
                func(*args, **kwagrs)
        return wrapper
    return my_deco

@repeat(3)
def say_hello():
    print("Hello---")

say_hello()