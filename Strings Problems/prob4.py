"""
Next higher palindromic number using the same set of digits

Given a palindromic number N in the form of string. The task is to find the smallest palindromic number greater than N using the same set of digits as in N.

Example 1:

Input: 
N = "35453"
Output: 
53435
Explanation: Next higher palindromic 
number is 53435.
Example 2:

Input: N = "33"
Output: -1
Explanation: Next higher palindromic number 
does not exist.
"""

def even(mid,N):
  a = N[mid]
  b = N[mid+1]
  if a > b:
     #4 > 3
    N[mid+1] = N[mid]
    left = N[0:mid]
    right = N[mid+2:]
    for i in range(len(left)):
      right[i] = left[-i-1]
      N[mid+2+i] = right[i]
    #print(left)
    #print(right)      
    return N
  else:
    #3 < 4
    N[mid] = str(int(N[mid]) + 1)
    left = N[0:mid+1]
    right = N[mid+1:]
    for i in range(len(left)):
      right[i] = left[-i-1]
      N[mid+1+i] = right[i]
    #print(left)
    #print(right)      
    return N
    
def odd(mid,N):
  return "working on it"

def nextPalin(N):
  N = list(N)
  l = len(N)
  mid = int(l/2-1)
  if l < 3:
    return "-1"
  elif l % 2 == 0: #even 
    return even(mid,N)
  else:
    return odd(mid,N)
  


if __name__ == "__main__":
  N = "33"
  print(N)
  for i in nextPalin(N):
    print(i,end='')

#solution 2

"""
def nextPalin(S):
        n = len(S)
        N = list(S)
        mid=(n//2)-1
        pos=-1
        for i in range(mid,0,-1):
            if N[i-1]<N[i] : 
                pos=i-1
                break
        
        if pos==-1 : 
            return "-1"
        
        numPos=-1;
        for i in range(pos+1,mid+1):
            if N[i]>N[pos]:
               if numPos==-1 :
                   numPos=i
               else :
                   if N[i]<N[numPos] :
                       numPos=i
    
        temp = N[pos]
        N[pos]=N[numPos]
        N[numPos]=temp

        N[pos+1:mid+1] = sorted(N[pos+1:mid+1])
        i=0
        j=n-1
        while i<=mid :
            N[j]=N[i]
            i+=1
            j-=1
        
        
        return ''.join(N)
    
if __name__ == "__main__":
    s = "35453"
    print(nextPalin(s))

"""
  