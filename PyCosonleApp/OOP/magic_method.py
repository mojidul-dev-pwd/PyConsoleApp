from PyCosonleApp.PolymorphismTest import Vehicle


##Basic magic methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} age is {self.age}"

    def __repr__(self):
        return f"Person(name={self.name},age={self.age})"
person = Person("Mojidul", 41)
print(person)
print(repr(person))

#operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x},{self.y})"
v1 = Vector(2,3)
v2 = Vector(4,5)

print(v1+v2)
print(v1-v2)
print(v1*v2)