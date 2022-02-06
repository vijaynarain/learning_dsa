"""
Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order. 

Examples:  

Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
Output: 4
Explanation: 
The subsequence 1, 3, 4, 2 is the longest 
subsequence of consecutive elements

Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
Output: 5
Explanation: 
The subsequence 36, 35, 33, 34, 32 is the longest 
subsequence of consecutive elements.
"""

def sequence():
  a.sort()
  num = 1
  j = 1
  for i in range(len(a)):
    if j <= len(a):
      if a[j] - a[i] == 1:
        num += 1
        j += 1
      if num == 1:
        num = 0
  return num


if __name__ == "__main__":
  a = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
  print(sequence())