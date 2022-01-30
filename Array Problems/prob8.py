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
a = [2, 5, 6]
b = [4, 6, 8, 10]

union = []
intersection = []

#new code complexity O(n)
i = 0
j = 0
n = min(len(a),len(b))

while n:
  if a[i] != b[j]:
    if a[i] in union:
      intersection.append(a[i])
      union.append(b[j])
    else:
      union.append(a[i])
      union.append(b[j])
  else:
    if a[i] not in union:
      union.append(b[j])
      intersection.append(b[j])
  i += 1
  j += 1
  n -= 1

if len(a) > len(b):
  for k in range(i,len(a)):
    union.append(a[k])
else:
  for k in range(j,len(b)):
    union.append(b[k])
    
    


#old code (complexity O(n^2))
"""
if len(a) > len(b):
  for i in range(len(a)):
    for j in range(len(b)):
      if a[i] == b[j]:
        intersection.append(a[i])
      else:
        A.append(a[i])
        A.append(b[j])
        #set function used to elimate duplicates
        union = set(A)""" 

print(union)
print(intersection)