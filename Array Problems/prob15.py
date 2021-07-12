"""
Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest. 

Examples: 

Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 [5 is the first element that repeats]

Input:  arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 [6 is the first element that repeats]
"""

def repeating_check(a):
  for i in range(len(a)):
    for j in range(1, len(a)):
      if a[i] == a[j]:
        return a[i]

if __name__ == "__main__":
  a = [6, 10, 5, 4, 9, 120, 4, 6, 10]
  print(f"This is first repeating number = {repeating_check(a)}")