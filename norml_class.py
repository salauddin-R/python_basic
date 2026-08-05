class paremtInfo:
    def __init__(self,name,age):
        print(f"My name is {name}, my age is {age}")
    def thisFamily(self,name,age):
        print(f"My name is {name}, my age is {age}")

p1=paremtInfo("Rony",44)
p1.thisFamily("Salauddin",23)

class understanding_method:
    def initialMethod(self):
        print("This is normal method")

    @classmethod
    def class_Method(cls):
        print("This is Calss Method")

    @staticmethod
    def static_Method():
        print("The method is Static Method")


p1 = understanding_method()
p1.initialMethod()
p1.static_Method()
understanding_method.class_Method()