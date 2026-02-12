from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print(" animal is sleeping...")

class Dog(Animal):

    def sound(self):
        print(" animal is Barking")

class Cat(Animal):
    def sound(self):
        print(" animal is Meowing")

class Cow(Animal):
    def sound(self):
        print(" animal is Mooing")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()

