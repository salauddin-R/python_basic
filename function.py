def addition(a,b):
    return a+b

print(addition(10,20))
print(addition(30,90))

def my_country(name="Bangladesh"):
    print(f"My country is {name}")

my_country("Saudi Arabia")
my_country()

def my_animal(animal,name):
    print(f"I have a animal that is {animal}.Name is {name}")
my_animal(animal="cow",name="Goru")

def my_functionii(name,/):
    print(f"My name is {name}")

my_functionii("Salauddin") #at sudu positional paramiter niba kono named paramiter niba na.

def my_functionP(*,name):
    print(f"My paramiter is {name}")

my_functionP(name="Rony")#accept only keyword argument

def data_function(a,b,/,*,c,d):
    return a+b+c+d

result = data_function(10,15,c=9,d=22)
print(f"sum is {result}")