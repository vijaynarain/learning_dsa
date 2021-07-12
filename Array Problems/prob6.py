"""
Given an array arr of integer elements, the task is to find the range and coefficient of range of the given array where: 
Range: Difference between the maximum value and the minimum value in the distribution. 
Coefficient of Range: (Max – Min) / (Max + Min).
Examples: 
 

Input: arr[] = {15, 16, 10, 9, 6, 7, 17} 
Output: Range : 11 
Coefficient of Range : 0.478261 
Max = 17, Min = 6 
Range = Max – Min = 17 – 6 = 11 
Coefficient of Range = (Max – Min) / (Max + Min) = 11 / 23 = 0.478261
Input: arr[] = {5, 10, 15} 
Output: Range : 10 
Coefficient of Range : 0.5 

"""

a = [15, 16, 10, 9, 6, 7, 17]
max = a[0]

for i in range(len(a)):
  if a[i] > max:
    max = a[i]

min = a[0]

for i in range(len(a)):
  if a[i] < min:
    min = a[i]

Range = max - min
Coefficient = (max - min) / (max + min)

print(f"Range = {Range}")
print(f"Coefficient = {Coefficient}")