"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Examples:  

Input: arr[]   = {2, 0, 2}
Output: 2

We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 2, 0, 4}
Output: 7

We can trap "3 units" of water between 3 and 2,
"1 unit" on top of bar 2 and "3 units" between 2 
and 4.  See below diagram also.

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
"""

def findWater(arr, n):
 
    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n
 
    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n
 
    # Initialize result
    water = 0
 
    # Fill left array
    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])
 
    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);
 
    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]
 
    return water
 
 
# Driver program
 
arr = [3, 0, 2, 0, 4]
n = len(arr)
print("Maximum water that can be accumulated is", findWater(arr, n))