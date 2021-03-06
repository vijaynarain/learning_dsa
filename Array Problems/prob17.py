"""
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance. 
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

Examples : 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
"""

#old code
def number_arrange():
  a.sort()

  i,j = 1,1
  while j < len(a):
    if a[j] > 0:
      break
    j+=1

  while(a[i] < 0 & j < len(a)):
    a[i],a[j] = a[j],a[i]
    i+=2
    j+=1

  return a

#new code//working in this code (Recursion code)
"""
b = []
def number_arrange(i,j,a):
  while a[j] > 0 and j < len(a) - 1:
    j += 1
  while a[i] < 0 and i < len(a) - 1:
    i += 1
  b.append(a[i])
  b.append(a[j])
  if j < len(a) - 1 and i < len(a) - 1:
      number_arrange(i+1, j+1, a)
  a = b
  return a
    
print(number_arrange(i=0,j=0,a=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))
"""
    

if __name__ == "__main__":
  a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
  print(f"Given Array = {a}")
  print(f"Arranged Array = {number_arrange()}")