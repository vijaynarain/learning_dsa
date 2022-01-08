def subseq(t,i,n,S):
    if i == n:
      print(t)
    else:
        subseq(t,i+1,n,S)
        t = t + S[i]
        subseq(t,i+1,n,S)
        
S = "abc"
subseq("",0,len(S),S)

"""
Main Algo:- 

1. first we pass data in funtion empty string to store value and index value '0' and length of string and also the string 
subseq("", 0, len(S), S)
2. now we handle two cases to get subsequence of string 
3. if traverse the whole string than we print substring 't'
4. else, we again pass function(recursion) wih increament of index to don't get first value
5. now we add remainig string to substring 
6. now, again we passing function with increasing index number
7. that's it
"""