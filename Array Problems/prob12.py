from collections import Counter
"""
Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.

Example: 

Input : n = 7 (length) and array[] = {1, 2, 3, 6, 3, 6, 1}
Output: 1, 3, 6

Explanation: The numbers 1 , 3 and 6 appears more
than once in the array.
"""

#old code complexity is O(n^2)
"""
def repetationCheck(a):
  for i in range(len(a)):
    for j in range(i+1, len(a)):
      if a[i] == a[j]:
        print("this number is repetative =",a[i])
"""

#new code complexity is O(n)
def repetationCheck(a):
  times = Counter(a)
  for i in times:
    if times[i] > 1:
      print(i)
  

if __name__ == "__main__":
  a = [1, 2, 3, 6, 3, 6, 1]
  repetationCheck(a)
  