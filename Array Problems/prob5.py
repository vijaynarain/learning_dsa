"""
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
Examples: 
 

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

"""

a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

print(a)

for i in range(len(a)):
  for j in range(i+1, len(a)):
    if a[i] > a[j]:
      a[i],a[j] = a[j],a[i]

print(a)