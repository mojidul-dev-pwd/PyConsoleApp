class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, fname, lname, age):
    self.fname = fname
    self.lname = lname
    self.age = age
  def __str__(self):
    return f"{self.fname} {self.lname} is now {self.age} years old."

  def myfunc(self):
      print("Hello my name is " + self.fname +' '+ self.lname)

  def print_full_name(self):
      print(self.fname, self.lname)

p1 = Person("Mojidul", "Islam",46)
print(p1)
print(p1.fname)
print(p1.age)
print(p1.myfunc())
p1.print_full_name()

#inheritace
class Student(Person):
  pass
x = Student("Nayeem", "Islam", 12)
x.print_full_name()

class Student(Person):
  def __init__(self, fname, lname, age):
      Person.__init__(self, fname, lname, age)
x = Student("Sarmin", "Jahan",12)
x.print_full_name()
#another way to inheritance
class Student(Person):
  def __init__(self, fname, lname, age):
      super().__init__(fname, lname, age)
      self.graduationyear = 2019

  def welcome(self):
      print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

x = Student("Nigar", "Jahan",12)
x.print_full_name()
print(x.graduationyear)
x.welcome()

#iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


