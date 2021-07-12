"""
Minimum number of jumps to reach end

Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, they cannot move through that element. If the end isn’t reachable, return -1.

Examples: 

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 -> 9)
Explanation: Jump from 1st element 
to 2nd element as there is only 1 step, 
now there are three options 5, 8 or 9. 
If 8 or 9 is chosen then the end node 9 
can be reached. So 3 jumps are made.

Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output: 10
Explanation: In every step a jump 
is needed so the count of jumps is 10.
"""


def minJump():
    maxR = a[0]
    step = a[0]
    jump = 1
    if (n == 1):
        return 0
    elif a[0] == 0:
        return -1
    else:
        for i in range(1, n):
            if i == n - 1:
                return jump
            maxR = max(maxR, i + a[i])
            step -= 1
            if step == 0:
                jump += 1
                if i >= maxR:
                    return -1
                step = maxR - i


if __name__ == "__main__":
    a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    n = len(a)
    print(f"Jump = {minJump()}")
