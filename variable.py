x,y,z="apple","banana","cherry"
print(x)
print(y)
print(z)

x=y=z="orange"
print(x)
print(y)
print(z)

fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

x="python"
y="is"
z="awesome" 
print(x,y,z)
print(x+y+z)

x=8
y=9
print(x+y)
z="rony"
#print(x+z)#string and integer cannot be added together

x="awesome"

def myFunc():
    x="fantastic"
    print("Python is ",x)

myFunc()
print("Python is ",x)

def myFunc2():
    global x 
    x = "fantastic"
    print("Python is ",x)

myFunc2()
print("Python is ",x)

#bytes
dataList=[1,2,3,4,5,6,7,8,9,10]
b=bytes(dataList)
print(type(b))
print(list(b))
#b[2]=9 byte muteable kono data change kora jai na.

#bytearry
b2=bytearray(b)
print(type(b2))
b2[4]=90
print(list(b2))

#None type
x = None
print(type(x))
print(x)