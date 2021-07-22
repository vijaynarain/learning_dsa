"""
Look and Say Pattern

Given an integer n. Return the nth row of the following look-and-say pattern.
1
11
21
1211
111221


Example 1:

Input:
n = 5
Output: 111221
Explanation: The 5th row of the given pattern
will be 111221.
Example 2:

Input:
n = 3
Output: 21
Explanation: The 3rd row of the given pattern
will be 21.
"""

def count(n):
  if n==1: return "1"
  if n==2: return "11"
  s = "11"
  for i in range(3,n+1):
    t = ""
    s += '&'
    c = 1
    for j in range(1,len(s)):
      if s[j] != s[j-1]:
        t += str(c)
        t += s[j-1]
        c = 1
      else:
        c+=1
    s = t
  return s



if __name__ == "__main__":
  n = 5
  print(count(n))