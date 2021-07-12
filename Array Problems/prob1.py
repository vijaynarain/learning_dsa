#program to find max and minimum in array

from array import array as arr

a = arr("i", [10, 30, 2, 12, 45, 1])

max = a[0]

for i in range(1, len(a)):
  if a[i]>max:
    max = a[i]

print(max)

min = a[0]

for i in range(1, len(a)):
  if a[i]<min:
    min = a[i]

print(min)
