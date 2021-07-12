"""

Given an array, cyclically rotate the array clockwise by one. 

Examples:  

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

"""

a = [1, 2, 3, 4, 5, 6, 9, 10]
print(a)
last = a[-1]
a.pop(-1)
a.insert(0,last)
print(a)