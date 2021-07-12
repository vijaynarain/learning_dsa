"""
A sorted array is rotated at some unknown point, find the minimum element in it. 
The following solution assumes that all elements are distinct.

Examples: 

Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1
"""
def find_minimum():
  min = a[0]
  for i in range(len(a)):
    if a[i] < min:
      min = a[i]
  return min

if __name__ == "__main__":
  a = [5, 6, 1, 2, 3, 4]
  print(find_minimum())