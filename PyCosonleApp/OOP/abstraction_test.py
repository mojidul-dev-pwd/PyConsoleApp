from abc import ABC, abstractmethod

## Abstract class

class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

def operate_vehicle(vehicle):
        vehicle.start_engine()
        vehicle.drive()
car = Car()
operate_vehicle(car)