def arbitrary_arg(*data2):
#     data=0
#     for i in data2:
#         data+=i
#     print(f"total data is {data}")


# arbitrary_arg(1,2,3,4,5)

# def Arbitrary_kwargs(**myData):
#     print(f"My name is {myData["name"]}")
#     print(f"My age is {myData["age"]}")
#     print(f"My village is {myData["village"]}")

# Arbitrary_kwargs(name="Salauddin",age=23,village="nurnagar")

# def my_function(title, *args, **kwargs):
#   print("Title:", title)
#   print("Positional arguments:", args)
#   print("Keyword arguments:", kwargs)

# my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# def my_Unpacking_Dictionaries(fname,lname):
#     print(f"My firs name is {fname}")
#     print(f"My lname name is {lname}")

# person = {"fname":"Salauddin","lname":"Rony"}
# my_Unpacking_Dictionaries(**person)

# x = 300
# def myfunc():
#   global x
#   x = 200
# myfunc()
# print(x)

# def myFun():
#     x = "Jane"
#     def myFunc():
#         nonlocal x
#         x="Hello"
#     myFunc()
#     return x
# print(myFun())

# x = "global"

# def outer():
#   x = "enclosing"
#   def inner():
#     x = "local"
#     print("Inner:", x)
#   inner()
#   print("Outer:", x)

# outer()
# print("Global:", x)

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())

# def changecase(n):
#   def changecase(func):
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(1)
# def myfunction():
#   return "Hello Linus"

# print(myfunction())

# numbers = [1,2,3,4,5]
# doubled = list(map(lambda x:x*2,numbers))
# print(doubled)

# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

# def my_Yield():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# for i in my_Yield():
#     print(i)
