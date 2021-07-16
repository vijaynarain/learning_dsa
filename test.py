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
