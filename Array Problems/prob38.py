"""
Longest Consecutive Subsequence

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

def longConse():
  max = 0
  num = 1
  for i in range(n-1):
      if a[i+1] - a[i] == 1:
        num+=1
      else:
        num = 1
      if max < num:
        max = num
  return max
      


if __name__ == "__main__":
  a = [1, 9, 3, 10, 4, 20, 2]
  n = len(a)
  a.sort()
  print("the longest subsequence of consecutive elements =",longConse())
