"""
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
Note: Order of elements is not important here.

"""

a = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

print(a)

for i in range(len(a)):
  for j in range(i+1, len(a)):
    if a[i] > a[j]:
      a[i],a[j] = a[j],a[i]

print(a)