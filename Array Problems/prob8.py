"""
Given two sorted arrays, find their union and intersection.
Example:

Input : arr1[] = {1, 3, 4, 5, 7}
        arr2[] = {2, 3, 5, 6} 
Output : Union : {1, 2, 3, 4, 5, 6, 7} 
         Intersection : {3, 5}

Input : arr1[] = {2, 5, 6}
        arr2[] = {4, 6, 8, 10} 
Output : Union : {2, 4, 5, 6, 8, 10} 
         Intersection : {6}

"""
a = [1, 3, 4, 5, 7]
b = [2, 3, 5, 6]

A = []
intersection = []

if len(a) > len(b):
  for i in range(len(a)):
    for j in range(len(b)):
      if a[i] == b[j]:
        intersection.append(a[i])
      else:
        A.append(a[i])
        A.append(b[j])
        union = set(A)

print(intersection)
print(union)