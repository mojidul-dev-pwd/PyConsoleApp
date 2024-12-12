## Encapsulation with getter and setter method
## public private protected
class Person:
    def __init__(self, name, age):
        self.name = name ##public variable
        self.age = age ## public variable

def get_name(person):
    return person.name
person = Person("Mojidul", 40)
print(person.name)

## private variable
# Not accessible outside the class
class PersonWithPrivateVariable:
    def __init__(self, name, age, gender):
        self.__name = name ##private variable
        self.__age = age ## private variable
        self.gender = gender ##public variable

    #getter method
    def get_name_private(self):
        return self.__name

    #setter method
    def set_name_private(self, name):
        self.__name = name

person_private = PersonWithPrivateVariable("Mojidul", 40, "Male")
print("Access Private Variable = ",person_private.get_name_private())
person_private.set_name_private("Nayeem")
print("Now Private Variable value is = ",person_private.get_name_private())
## print("Shows error if you try to access = ",person_private.__name)
print("Access only public variable = ",person_private.gender)
"""
def get_name(person):
    return person.__name
person_private = PersonWithPrivateVariable("Mojidul", 40, "Male")
print(person_private.name)
"""
## protected variable
# Accessible from the derived class
class PersonWithProtectedVariable:
    def __init__(self, name, age, gender):
        self._name = name ##protected variable
        self._age = age ## protected variable
        self.gender = gender ##public variable

class Employee(PersonWithProtectedVariable):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

employee = Employee("Mojidul", 40, "Male")
print("Access from derived class = ",employee._name)

