class class1:
    def class1_fun(self):
        print("This is class 1")

class class2(class1):
    def class2_fun(self):
        print("This is class 2")

class class3(class2):
    def class3_fun(self):
        print("This is class 3")


p1=class3()
p1.class3_fun()
p1.class2_fun()
p1.class1_fun()
