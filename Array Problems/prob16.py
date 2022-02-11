"""
Given an array with all distinct elements, find the largest three elements. Expected time complexity is O(n) and extra space is O(1). 
Examples :

Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23
"""

#old code
"""
def checking():
  for i in range(len(a)):
    for j in range(len(a)):
      if a[i] > a[j]:
        a[j],a[i] = a[i],a[j]
  print(a[0],a[1],a[2])
"""

#new code this have less complexity than previous
#this using Bubble sort algorithm
def checking():
  n = len(a)
  for i in range(n):
    swapped = False
    for j in range(n-i-1):
      if a[j+1] < a[j]:
        swapped = True
        a[j+1],a[j] = a[j],a[j+1]
        print(a)
    if swapped:
      break

  print(a[n-3:])

if __name__ == "__main__":
  a = [10, 4, 3, 50, 23, 90]
  checking()