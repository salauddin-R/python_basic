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
