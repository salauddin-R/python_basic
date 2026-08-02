#List Data -- this is mutable or changable
listData = [1,2,3,4,5,6,7,8,9]
print(listData)
listData[0]=99
print(listData)


#Tuple Data -- this is immutable or unchangeable
tupleData = (1,2,3,4,5,6,7,8) #this use parent thesis or ()
#trupleData[2]=4 #truple unchangeable
print(tupleData)

#range -- take 0 t0 rangeData-1
rangeData = range(9)
for i in rangeData:
    print(i,end=",") # end="" print it in a row

#spacify the data type
x = str("\nHello World")
y = list((1,2,3,4,5))
z = tuple((1,2,3,4,5))
a = bytes((1,2,3,4,5))
print(x)
print(y)
print(z)
print(list(a))