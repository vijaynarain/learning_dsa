"""
Given an array arr[], find the maximum j – i such that arr[j] > arr[i]

Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

Examples : 

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1 
"""

def maxiIndex():
  max = 0
  differ = 0
  for i in range(len(a)):
    for j in range(1,len(a)):
      differ = j - i
      if a[j] > a[i]:
        if max < differ:
          max = differ
  return max


if __name__ == "__main__":
  a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
  print(maxiIndex())