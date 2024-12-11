class Car:
    def __init__(self, windows, doors, engine_types):
        self.windows = windows
        self.doors = doors
        self.engine_types = engine_types

    def drive(self):
        print(f"The person will drive the {self.engine_types} Car")

car1 = Car(4,3, "Petrol")
print(car1.drive())

class Tesla(Car):
    def __init__(self, windows, doors, engine_types, is_self_driving):
        super().__init__(windows, doors, engine_types)
        self.is_self_driving = is_self_driving

    def self_driving(self):
        print(f"Tesla support's self driving: { self.is_self_driving}")

tesla = Tesla(4,3,"Diesel", True)
tesla.self_driving()
tesla.drive()

##multiple inheritance
## Base class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Subclass must implemented this class.")

## Base class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner

##Derived class
class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} say woof."

dog = Dog("Buddy1", "Thomas")
print(dog.speak())
print(f"{dog.owner} is Owner.")