thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

print(thisdict)
print(thisdict["year"])

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(thisdict.keys())
thisdict["country"]="BanglaDesh"
print(thisdict.values())
thisdict.update({"age": 2020})
x=thisdict.items()
print(x)
thisdict.pop("name")
thisdict.popitem()#delete the last item
thisdict.clear()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
for y in thisdict.keys():
  print(y)

for x,y in thisdict.items():
  print(f"\"{x}\":\"{y}\"")

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x,obj in myfamily.items():
    print(x)

    for y in obj:
        print(y+ ":", obj[y])