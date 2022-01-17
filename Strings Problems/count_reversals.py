import math
def countRev(s):
    # your code here
    n = len(s)
    if n%2 != 0: return -1
    o = 0 #o = opening bracket
    c = 0 #c = closing bracket
    rev = 0 #checking for times of reversal
    for i in range(n):
        if s[i] == "{":
            o += 1  #if we get opening, than we increase o
        else:
            if o == 0:  #if o is 0, means till now parathesisi is balanced
                c += 1  #if o is 0, than we get extra c
            else:
                o -= 1  #if o is not 0 and not the '{', than we have to decrease the o

    #this add all the ceiling value of o and c
    #'}{{{' o = 3, c = 1. (o/2.0 + c/2.0) = 3
    rev = int(math.ceil(o/2.0) + math.ceil(c/2.0))
    
    return rev

print(countRev("}{{}}{{{"))

