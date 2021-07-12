"""Given an array, a[], and an element x, find a number of occurrences of x in a[].
Examples: 
 

Input  : a[] = {0, 5, 5, 5, 4}
           x = 5
Output : 3

Input  : a[] = {1, 2, 3}
          x = 4
Output : 0
"""

a = [1, 2, 3, 3, 3, 4, 5]

x = int(input("Enter number which you want to find = "))
count = 0

for i in range(len(a)):
  if x == a[i]:
    count = count + 1
    
print(count)

print(f"Your number {count} times appeare in array")
