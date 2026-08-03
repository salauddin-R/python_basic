#String learning
print('hi this is "Salauddin" I live in #nurnagar. My emplee id is $:20607\n')

x = 100
print(f"I am {x}% sure that he is lyer")

a = """this is md salauddin rony.
I am a student of Northern University Bangladesh.
I am proud to join sparkTechAgency as a flutter developer.
It make me as a professonal developer"""
print(a)
print(a[2])
print("is" in a)

for x in "banana":
    print(x)

b = "Hellow world"
print(b[1:4])
print(b[:5])
print(b[2:])
print(b[-6:-2])#indexing start right -1 to left.data will -3 to -6.


#Modify String
age=45
print(f"My name is John, I am {age}")
x="Hello, World"
print(x.replace("Hello","hi"))
print(x.split(","))
print(x.upper())
print(x.lower())
w="  Hello World  "
print(w.strip())#remove xtra space from start and end

result = 5.43543
print(f"the result is {result:0.2f}")

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

