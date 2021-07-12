"""
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

Examples: 

Input: 
ar1[] = {1, 5, 10, 20, 40, 80} 
ar2[] = {6, 7, 20, 80, 100} 
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
Output: 20, 80

Input: 
ar1[] = {1, 5, 5} 
ar2[] = {3, 4, 5, 5, 10} 
ar3[] = {5, 5, 10, 20} 
Output: 5, 5
"""

def elements_check(arr1, arr2, arr3):
  pass
  for i in range(len(arr1)):
    for j in range(len(arr2)):
      for k in range(len(arr3)):
        if arr1[i] == arr2[j] & arr1[i] == arr3[k]:
          print(f"This Element is common = {arr1[i]}") 

if __name__ == "__main__":
  arr1 = [1, 5, 10, 20, 40, 80]
  arr2 = [6, 7, 20, 80, 100]
  arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
  elements_check(arr1, arr2, arr2)