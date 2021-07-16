"""
Reverse words in a given string

Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i
Example 2:

Input:
S = pqr.mno
Output: mno.pqr
Explanation: After reversing the whole
string , the input string becomes
mno.pqr
"""

def reverseWords():
  S = "i.like.this.program.very.much"
  ans = " "
  i = len(S) - 1
  while i >= 0:
    while i >= 0 and S[i] == ".":
      i -= 1
    j = i
    if i < 0: break
    while i >= 0 and S[i] != ".":
      i -= 1
    if ans == " ":
      ans += S[i+1:j+1]
    else:
      ans += "." + S[i+1:j+1]
  return ans
      

print(reverseWords())

