import random
#tester
list0 = [1,2,3,4,5,6,7]
random.shuffle(list0)
print(list0)

#returns 2d list, evenly split, 0th index gets more if odd number of items to be sorted
def hack(p):
  output = [[],[]]
  for item in p:
    if len(output[1]) < len(output[0]):
      output[1] += [item]
    else:
      output[0] += [item]
  return output

#combines 2 lists, 0th indexes are compared then popped to output, then the sorted remainder is appended to the end.
def combine(a,b):
  output = []
  while a != [] and b != []: #repeat until one side has remainder
    if a[0] < b[0]:
      output.append(a.pop(0))
    else:
      output.append(b.pop(0))
  output += a #add remainder, its fine to add an empty list to a list
  output += b
  return output

#splits apart list, calls to split it further if possible, then puts returned sorted pieces together.
def mergesort(a):
  a = hack(a)
  if len(a[0]) > 1:
    a[0] = mergesort(a[0])
  if len(a[1]) > 1:
    a[1] = mergesort(a[1])
  return combine(a[0],a[1])

print(mergesort(list0))