"""
Given an array that contains both positive and negative integers, find the product of the maximum product subarray. Expected Time complexity is O(n) and only O(1) extra space can be used.

Examples:

Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -40, 0, -2, -3}
Output:   80  // The subarray is {-2, -40}
"""

def product():
    minval = a[0]
    maxval = a[0]
    result = a[0]
    
    for i in range(1,len(a)):
        if a[i] < 0:
          minval,maxval = maxval,minval
        
        maxval = max(a[i], maxval * a[i])
        minval = min(a[i], minval * a[i])
        
        if maxval > result:
            result = maxval
    
    return result
    
    
if __name__ == "__main__":
    a = [6, -3, -10, 0, 2]
    print(product())
