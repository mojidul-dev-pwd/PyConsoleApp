from abc import ABC, abstractmethod

#Base class

class Animal:
    def speak(self):
        return "Sound of the Animal."

#Derived class 1
class Dog(Animal):
    def speak(self):
        return "woof"

#Derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow"

##Functions that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)
animal_speak(cat)

##Polymorphysm with functions and methods
#Base class
class Shape:
    def area(self):
        return "The area of the figure"
#Derived class 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
#Derived class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

##Write a function which demonstrate polymorphism
def print_area(shape):
    print(f"The area is {shape.area()}")

rect = Rectangle(4, 5)
print_area(rect)
cir = Circle(3)
print_area(cir)

##Polymorphysm with Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class CCar(Vehicle):
    def start_engine(self):
        return "Car engine started"
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

##Functions that demonstrates polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())

ccar = CCar()
motorcycle = Motorcycle()
start_vehicle(ccar)
start_vehicle(motorcycle)
