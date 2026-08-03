thisList = ["apple","banana","cherry"]
for x in thisList:
    print(x)

for y in range(len(thisList)):
    print(thisList[y])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
newList2 = fruits
print(newList2)
print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
    return abs(n-50)
thisList=[100,50,65,82,23]
thisList.sort(key = myfunc)
print(thisList)

thisList=[100,50,65,82,23]
myList=thisList.copy()
print(myList)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

fruits = ["apple", "cherry", "banana", "cherry"]
x = fruits.count("cherry")
print(x)
x = fruits.index("apple")
print(x)

#Add two tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)