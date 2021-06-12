from array import array

a = array('i', [1,3,4,5])

def printArray():
  for i in range(len(a)):
    print(a[i], end=" ")
  print("\n")

printArray()

a.insert(1,2)

printArray()

a.append(6)

printArray()

a.remove(1)

printArray()

a.pop(0)

printArray()

