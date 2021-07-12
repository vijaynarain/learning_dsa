"""
Longest alternating subsequence

A sequence {x1, x2, .. xn} is alternating sequence if its elements satisfy one of the following relations : 

  x1 < x2 > x3 < x4 > x5 < …. xn or 
  x1 > x2 < x3 > x4 < x5 > …. xn
Examples :

Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3 

Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form 
x1 < x2; or x1 > x2

Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest subsequence of length 6.
"""

def LAS(arr, n):
   
    # "inc" and "dec" initialized as 1
    # as single element is still LAS
    inc = 1
    dec = 1
     
    # Iterate from second element
    for i in range(1,n):
       
        if (arr[i] > arr[i-1]):
           
            # "inc" changes iff "dec"
            # changes
            inc = dec + 1
        elif (arr[i] < arr[i-1]):
           
            # "dec" changes iff "inc"
            # changes
            dec = inc + 1
             
    # Return the maximum length
    return max(inc, dec)
 
# Driver Code
if __name__ == "__main__":
    arr = [10, 22, 9, 33, 49, 50, 31, 60]
    n = len(arr)
     
    # Function Call
    print(LAS(arr, n))