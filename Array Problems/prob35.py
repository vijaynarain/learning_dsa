"""
Find the repeating and the missing | Added 3 new methods

Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

Examples: 

 Input: arr[] = {3, 1, 3}
Output: Missing = 2, Repeating = 3
Explanation: In the array, 
2 is missing and 3 occurs twice 

Input: arr[] = {4, 3, 6, 2, 1, 1}
Output: Missing = 5, Repeating = 1
"""

def findingNumber():
  csum = 0
  rsum = n
  repeat = 0
  for j in range(n):
      rsum += j
      csum += a[j]
      if a[j-1] - a[j] == 0:
        repeat  = a[j]
  missing = rsum - csum + repeat

  #print(rsum)
  #print(csum)
  print("Missing =",missing)
  print("Repeat Number=", repeat)


    

if __name__ == "__main__":
  a = [4, 3, 6, 2, 1, 1]
  n = len(a)
  findingNumber()