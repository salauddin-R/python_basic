dataSet = {"apple","banana","banana","mango"}
dataSet.add("pinapple")
print(dataSet)

dataList={"Goava","chili"}
dataSet.update(dataList)
print(dataSet)

dataSet.remove("banana")
print(dataSet)
print(dataSet.pop())
print(dataSet.clear())

set1 = {1,2,3,"a","b","b"}
set2 = {2,3,"b","v","d","g"}
print(set1.update(set2))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference_update(set2))