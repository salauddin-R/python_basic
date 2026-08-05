class self_class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def self_second(self):
        print("Hello, my name is "+self.name)
p1 = self_class("Rony",23)
p1.self_second()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)

class Person:
  lastname = ""
  def __init__(self, name):
    self.name = name
Person.lastname = "Refsnes"
p1 = Person("Linus")
p2 = Person("Emil")
print(p1.lastname)
print(p2.lastname)

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")
p1.age=23
p1.city="Dhaka"
print(p1.name)
print(p1.age)
print(p1.city)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):#return with out calling
    return f"{self.name} ({self.age})"
p1 = Person("Tobias", 36)
print(p1)
