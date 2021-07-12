"""
Given heights of n towers and a value k. We need to either increase or decrease the height of every tower by k (only once) where k > 0. The task is to minimize the difference between the heights of the longest and the shortest tower after modifications and output this difference.
Examples: 

Input  : arr[] = {1, 15, 10}, k = 6
Output :  Maximum difference is 5.
Explanation : We change 1 to 7, 15 to 
9 and 10 to 4. Maximum difference is 5
(between 4 and 9). We can't get a lower
difference.

Input : arr[] = {1, 5, 15, 10} 
        k = 3   
Output : Maximum difference is 8
arr[] = {4, 8, 12, 7}

Input : arr[] = {4, 6} 
        k = 10
Output : Maximum difference is 2
arr[] = {14, 16} OR {-6, -4}

Input : arr[] = {6, 10} 
        k = 3
Output : Maximum difference is 2
arr[] = {9, 7} 

Input : arr[] = {1, 10, 14, 14, 14, 15}
        k = 6 
Output: Maximum difference is 5
arr[] = {7, 4, 8, 8, 8, 9} 

Input : arr[] = {1, 2, 3}
        k = 2 
Output: Maximum difference is 2
arr[] = {3, 4, 5} 
"""

def max_min(a):
  max = a[0]
  min = a[0]
  for i in range(len(a)):
    if a[i] > max:
      max = a[i]
    if a[i] < min:
      min = a[i]
  diff = max - min
  print(f"max = {max}")
  print(f"min = {min}")
  print(f"diff = {diff}")
  return diff

def minimise_tower_diff():
  diff = max_min(a)
  for i in range(len(a)):
    if diff-k >= a[i] + k:
      a[i] = a[i] + k
    else:
      a[i] = a[i] - k
  print(f"Tower Updated heights = {a}")
  tower_diff  = max_min(a)
  return tower_diff
    

if __name__ == "__main__":
  a = [1, 10, 14, 14, 14, 15]
  k = 6
  diff = 0
  print(f"Initial Tower heights = {a}")
  print(f"The tower diffrence = {minimise_tower_diff()}")