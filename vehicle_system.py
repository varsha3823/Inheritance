from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        print("Car engine started with a key or push button.")

class Bike(Vehicle):

    def start_engine(self):
        print("Bike engine started with a self-start or kick.")

class Bus(Vehicle):

    def start_engine(self):
        print("Bus engine started with a heavy-duty ignition system.")

car = Car()
bike = Bike()
bus = Bus()

car.start_engine()
bike.start_engine()
bus.start_engine()
