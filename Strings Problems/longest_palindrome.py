def longestPalin(S):
    # code here
    start = 0
    end = 0
    def expandFromCenter(S,i,j):
        while i >= 0 and j < len(S) and S[i] == S[j]:
            i = i - 1
            j = j + 1
        return j - i - 1
            
            
    for i in range(len(S)):
        len1 = expandFromCenter(S,i,i+1)
        len2 = expandFromCenter(S,i,i)
        length = max(len1,len2)
        if end - start < length:
            start = i - int((length-1)/2)
            end = i + int(length/2)
     
    #print(length)
    if len(S[start:end+1]) < 2:
        return S[0]
    else:
        return S[start:end+1]

S = "aaaabbaa"
print('Given String :',S)
print('Longest Palindrome :',longestPalin(S))
