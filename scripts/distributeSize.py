import random

print("---- DISTRIBUTE AN ARRAY OF COUNTS ----\n")

maxCount = 5;

def redistributeToMaxCount(list):
    listMax = max(list)

    return [((x / listMax) * maxCount) for x in list]

    for i in range(0, len(lst), n):
        yield lst[i:i + n]

list5 = [random.randint(0,10) for i in range(5)]
list5max = max(list5)
newList = [((x / list5max) * maxCount) for x in list5]

print(list5)
print(newList)


list1 = [random.randint(0,10) for i in range(1)]
list1max = max(list1)
print(list1)