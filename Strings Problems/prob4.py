"""
Next higher palindromic number using the same set of digits

Given a palindromic number N in the form of string. The task is to find the smallest palindromic number greater than N using the same set of digits as in N.

Example 1:

Input: 
N = "35453"
Output: 
53435
Explanation: Next higher palindromic 
number is 53435.
Example 2:

Input: N = "33"
Output: -1
Explanation: Next higher palindromic number 
does not exist.
"""

def nextPalin(N):
  l = len(N)
  isEven = l%2 == 0
  leftHalf = N[:int(l/2)]
  reversedigi = leftHalf[::-1]
  number = ""
  #print(leftHalf)
  #print(reversedigi)
  if isEven:
    number = reversedigi + leftHalf
  else:
    middigi = N[int(l/2)]
    number = reversedigi + middigi + leftHalf

  if number <= N:
    newNumb = int(int(N)/100)
    newNumb += 1
    newNumb = str(newNumb * 100)
    #print(newNumb)
    nextPalin(newNumb)
  
  return number
    

if __name__ == "__main__":
  N = "4282"
  print(N)
  print(nextPalin(N))
  



  