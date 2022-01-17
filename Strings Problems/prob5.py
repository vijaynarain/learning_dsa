"""
Longest Prefix Suffix 

Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

Example 1:

Input: s = "abab"
Output: 2
Explanation: "ab" is the longest proper 
prefix and suffix. 
Example 2:

Input: s = "aaaa"
Output: 3
Explanation: "aaa" is the longest proper 
prefix and suffix. 

reffrence video:- https://youtu.be/vTMXv-thazI
"""

def longPreSuf(s):
  A = [0 for i in range(len(s))]
  j = 0;i = 1
  while i < len(s) :
      if s[i] == s[j]:
          A[i] = j+1
          j+=1
          i+=1
      else :
          if j==0 :
              i+=1
          else :
              j = A[j-1]
  return A[-1]

if __name__ == "__main__":
  s = "abab"
  print(longPreSuf(s))

"""
Main Algo:- 
1. It's basically a part of KMP algorithm
2. it's a pre prossesing part of KMP
3. 
"""

