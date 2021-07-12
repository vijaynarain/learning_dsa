"""
Given an array with all distinct elements, find the largest three elements. Expected time complexity is O(n) and extra space is O(1). 
Examples :

Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23
"""

def checking():
  for i in range(len(a)):
    for j in range(len(a)):
      if a[i] > a[j]:
        a[j],a[i] = a[i],a[j]
  print(a[0],a[1],a[2])

if __name__ == "__main__":
  a = [10, 4, 3, 50, 23, 90]
  checking()