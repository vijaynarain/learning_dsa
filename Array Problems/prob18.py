"""
Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.

Examples : 

Input: {4, 2, -3, 1, 6}
Output: true 
Explanation:
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true 
Explanation:
There is a subarray with zero sum from index 2 to 2.

Input: {-3, 2, 3, 1, 6}
Output: false
"""

def sum_zero_check():
  for i in range(len(a)):
    j = i+1
    while j < len(a):
      if a[i] == 0:
        return "True"
      a[i] = a[i] + a[j]
      if a[i] == 0:
        return "True"
      j+=1
  return "False"


if __name__ == "__main__":
  a = [-3, 2, 3, 1, 6]
  print(sum_zero_check())