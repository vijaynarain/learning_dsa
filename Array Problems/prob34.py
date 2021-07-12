"""
Maximum Sum Path in Two Arrays

Given two sorted arrays, such that the arrays may have some common elements. Find the sum of the maximum sum path to reach from the beginning of any array to end of any of the two arrays. We can switch from one array to another array only at common elements. 
Note: The common elements do not have to be at the same indexes.

Expected Time Complexity: O(m+n), where m is the number of elements in ar1[] and n is the number of elements in ar2[].

Examples: 

Input: ar1[] = {2, 3, 7, 10, 12}
       ar2[] = {1, 5, 7, 8}
Output: 35

Explanation: 35 is sum of 1 + 5 + 7 + 10 + 12.
We start from the first element of arr2 which is 1, then we
move to 5, then 7.  From 7, we switch to ar1 (as 7 is common)
and traverse 10 and 12.

Input: ar1[] = {10, 12}
       ar2 = {5, 7, 9}
Output: 22

Explanation: 22 is the sum of 10 and 12.
Since there is no common element, we need to take all 
elements from the array with more sum.

Input: ar1[] = {2, 3, 7, 10, 12, 15, 30, 34}
        ar2[] = {1, 5, 7, 8, 10, 15, 16, 19}
Output: 122

Explanation: 122 is sum of 1, 5, 7, 8, 10, 12, 15, 30, 34
"""


def maximumSumPath():

    i, j = 0, 0
    result, sum1, sum2 = 0, 0, 0

    while (i < m and j < n):

        if a[i] < b[j]:
            sum1 += a[i]
            i += 1

        elif a[i] > b[j]:
            sum2 += b[j]
            j += 1

        else:
            result += max(sum1, sum2) + a[i]
            sum1 = 0
            sum2 = 0

            i += 1
            j += 1

    while i < m:
        sum1 += a[i]
        i += 1
    while j < n:
        sum2 += b[j]
        j += 1

    result += max(sum1, sum2)

    return result


if __name__ == "__main__":
    a = [2, 3, 7, 10, 12, 15, 30, 34]
    b = [1, 5, 7, 8, 10, 15, 16, 19]
    m = len(a)
    n = len(b)
    print("Maximum sum path is",maximumSumPath())
