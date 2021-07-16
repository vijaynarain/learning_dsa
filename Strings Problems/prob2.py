"""
Longest Common Prefix in an Array

Given a array of N strings, find the longest common prefix among all strings present in the array.

Example 1:

Input:
N = 4
arr[] = {geeksforgeeks, geeks, geek,
         geezer}
Output: gee
Explanation: "gee" is the longest common
prefix in all the given strings.
â€‹Example 2:

Input: 
N = 2
arr[] = {hello, world}
Output: -1
Explanation: There's no common prefix
in the given strings than return -1
"""

def prefix():
  n = 4
  i = 0
  j = 0
  result = ""
  datacheck = ""
  arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
  #print(len(arr[i]))
  while True:
    while i < n - 1 and j < len(arr[i]):
      datacheck = arr[i][j]
      i+=1
      if datacheck == arr[i][j]:
        continue
      else:
        break
    if datacheck != arr[i][j]:
      return result 
    result += datacheck
    j += 1
    i = 0

print(prefix()) 