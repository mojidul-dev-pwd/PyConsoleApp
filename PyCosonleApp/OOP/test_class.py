class Car:
    pass

audi = Car()
prado = Car()

print(type(audi))
print(audi)

audi.window = 4

print(audi.window)

class Dog:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof.")

dog1 = Dog("Buddy", 3)
print(dog1)
print(dog1.name)
print(dog1.age)

## Class with an instance method
dog1.bark()
dog2 = Dog("kutta", 4)
dog2.bark()

### Model for a bank account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn. New balance is {self.balance}")

    def get_balance(self):
        return self.balance

account = BankAccount("Mojidul", 10000)
print(account.balance)
account.deposit(20000)
print(account.balance)
account.withdraw(1000)
print("Now Balance is ", account.get_balance())