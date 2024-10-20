from array import *

# python array buitin type
arr1 = array('i',[23,234,4546])   # first we define the type of values to be stord and then only store those values in list.
print(type(arr1))

# iterating over the array
for i in arr1:
    print(i)

for a in range(len(arr1)):
    print(a)

for a in range(len(arr1)):
    print(arr1[a])


