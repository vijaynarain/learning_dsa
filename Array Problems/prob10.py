"""
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

Example: 

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
Output: 5
Explanation: The missing number from 1 to 8 is 5

Input: arr[] = {1, 2, 3, 5}
Output: 4
Explanation: The missing number from 1 to 5 is 4
"""

#old code
"""
def getMissingNumber(A):
 
    # Compute XOR of all the elements in the list
    xor = 0
    for i in A:
        xor = xor ^ i
 
    # Compute XOR of all the elements from 1 to `n+1`
    for i in range(1, len(A) + 2):
        xor = xor ^ i
 
    return xor
"""

#new code
def getMissingNumber(A):
  count = 1
  for i in range(len(A)):
    if count in A:
      count += 1
    else:
      return count
 
if __name__ == '__main__':
 
    A = [1, 2, 4, 6, 3, 7, 8]
    print("The missing number is", getMissingNumber(A))