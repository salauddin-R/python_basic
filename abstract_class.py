from abc import ABC,abstractmethod

class Animal_Class(ABC):
    def normal_method(self):
        print("This is normal method")

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal_Class):
    def sound(self):
        print("Woof")

d = Dog()
d.sound()
d.normal_method()