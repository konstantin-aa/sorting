import random

list0 = [1,2,3,4,5,6]
random.shuffle(list0)
print('dermatologists hate it! destroy them all with this one simple trick! before:', list0)
def quicksort(alist):
  if len(alist) > 0:
    middle = alist.pop(0)
    side1 = []
    side2 = []
    for number in alist:
      if number <= middle:
        side1 += [number]
      else:
        side2 += [number]
    side1 = quicksort(side1)
    side2 = quicksort(side2)
    alist = side1 + [middle] + side2
  return alist

print('after:', quicksort(list0))