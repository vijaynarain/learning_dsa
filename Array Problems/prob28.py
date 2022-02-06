"""
*Important:-

Print a given matrix in spiral form

Given a 2D array, print it in spiral form. See the following examples.

Examples: 

Input:  1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16

Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
Explanation: The output is matrix in spiral format. 

Input:  1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18

Output: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
Explanation :The output is matrix in spiral format.
"""

def printdata(arr, i, j, m, n):
    #m=Row, n=Collumn 
    # If i or j lies outside the matrix
    if (i >= m or j >= n):
        return
 
    # Print First Row
    for p in range(i, n):
        print(arr[i][p], end=" ")
 
    # Print Last Column
    for p in range(i + 1, m):
        print(arr[p][n - 1], end=" ")
 
    # Print Last Row, if Last and
    # First Row are not same
    if ((m - 1) != i):
        for p in range(n - 2, j - 1, -1):
            print(arr[m - 1][p], end=" ")
 
    # Print First Column, if Last and
    # First Column are not same
    if ((n - 1) != j):
        for p in range(m - 2, i, -1):
            print(arr[p][j], end=" ")
 
    printdata(arr, i + 1, j + 1, m - 1, n - 1)
 
 

if __name__ == "__main__":
  
  arr = [[1,   2,   3,   4],
        [ 5,   6,   7,   8],
        [ 9,   10,  11,  12],
        [ 13,  14,  15,  16]]
  
  R = 4
  C = 4
  printdata(arr, 0, 0, R, C)
