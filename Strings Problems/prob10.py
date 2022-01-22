"""
Longest K unique characters substring

Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

Example 1:

Input:
S = "aabacbebebe", K = 3
Output: 7
Explanation: "cbebebe" is the longest 
substring with K distinct characters.
â€‹Example 2:

Input: 
S = "aaaa", K = 2
Output: -1
Explanation: There's no substring with K
distinct characters.
"""

def longestKSubstr():
  i,j,length,count = 0,0,0,0
  max_length = 0

  n = len(S)
  while j < n:
    while count <= K and j < n:
      if S[i] != S[j]:
        count += 1
      j+=1
    length = j - i
    i+=1
    j = i+1
    if length > max_length:
      max_length = length
  if count < K:
    return -1
  return max_length

if __name__ == "__main__":
  S = "hq"
  K = 2
  print(longestKSubstr())

"""
def longestKSubstr(S):
    table = dict(Counter(S))
    #print(table)
    length,max_lenght = 0,0
    i,j = 0,0
    n = len(S)
"""
