"""
Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.

Examples:  

Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  arr[] = {1, 5, 7, -1, 5}, 
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)         
"""

def pairChecking(a, sum, pair):
  print("pair checking for",a)
  print("sum =",sum)
  for i in range(0, len(a)):
    #print("i=",i)
    for j in range(i+1, len(a)):
      #print("j =",j)
      if sum == a[i] + a[j]:
        pair += 1
  return pair



if __name__ == '__main__':
  a = [1, 5, 7, -1, 5]
  sum = 6
  pair = 0
  #print("length = ",len(a))
  print("the numbers of pairs =",  pairChecking(a, sum, pair))
  