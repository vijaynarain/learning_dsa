"""
Find the row with maximum number of 1s

Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s. 

Example:  

Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  // this row has maximum 1s
0 0 0 0

Output: 2
"""

#main logic
def findOnesMax():
    mv = 0                  #maximum value
    mvr = 0                 #maximum value row
    for i in range(len(a)):
        num = 0
        for j in range(len(a)):
            if a[i][j] / 1 == 1:
                num += 1
        if mv < num:
            mv = num
            mvr = i
    print(f"Maximum value is {mv} in row {mvr}")


if __name__ == "__main__":
    #given matrix
    a = [[0, 1, 1, 1], 
         [0, 0, 1, 1],
         [1, 1, 1, 1], 
         [0, 0, 0, 0]]

    findOnesMax()
