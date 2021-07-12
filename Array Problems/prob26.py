"""
Find a triplet that sum to a given value

Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. If there is such a triplet present in array, then print the triplet and return true. Else return false.

Examples: 
 

Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
Output: 12, 3, 9 
Explanation: There is a triplet (12, 3 and 9) present 
in the array whose sum is 24. 
Input: array = {1, 2, 3, 4, 5}, sum = 9 
Output: 5, 3, 1 
Explanation: There is a triplet (5, 3 and 1) present 
in the array whose sum is 9.
"""


def calculate():
    i = 0
    n = 1
    j = 2
    while True:
        if i < len(a) - 1:
            sum = a[i] + a[n] + a[j]
            if sum == num:
                return (f"number = {a[i]} {a[n]} {a[j]}")
            else:
                if j < len(a) - 1 and n < len(a) - 1:
                    j += 1
                else:
                    n += 1
                    j = n + 1
        elif n == len(a) - 1 and j == len(a):
            i += 1


if __name__ == "__main__":
    a = [3, 12, 4, 1, 6, 9]
    num = 24
    print(f"Array = {a}")
    print(f"sum = {num}")
    print(calculate())
