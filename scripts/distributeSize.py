import random

print("---- DISTRIBUTE AN ARRAY OF COUNTS ----\n")

maxCount = 10;

def redistributeToMaxCount(list):
    listMax = max(list)
    return [((x / listMax) * maxCount) for x in list]

list5 = [random.randint(0,100) for i in range(10)]
list5max = max(list5)
newList = redistributeToMaxCount(list5)

print(list5)
print(newList)


list1 = [random.randint(0,10) for i in range(1)]
list1max = max(list1)
print(list1)