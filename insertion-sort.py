import random
#tester
list0 = [1,2,3,4,5,6,7]
random.shuffle(list0)
print(list0)

#insert selected object into the sorted list
def addIn(index0, processed):
  for index, item in enumerate(processed):
    if item > index0:
      processed.insert(index,index0)
      return processed
  processed.append(index0)
  return processed

#loop for inserting
def insertionSort(list0):
  temp = []
  for item in list0:
    temp = addIn(item,temp)
  return temp

print(insertionSort(list0))
