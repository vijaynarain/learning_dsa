"""
Given an array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3. 

a = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
times = n/k (n = size of array, k = given number)
times = 8/4 => 2 (more than 2 times no. in a)
result = 2,3
"""

def times_check():
  n = len(a)
  times = n/k
  for i in range(n):
    num = 1
    for j in range(i+1,n):
      if a[i] / a[j] == 1:
        num += 1
    if num > times:
      print(a[i])


if __name__ == "__main__":
  a = [3, 1, 2, 2, 1, 2, 3, 3,]
  k = 4
  times_check()
