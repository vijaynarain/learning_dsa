"""Given a binary string, that is it contains only 0s and 1s. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped.

Example 1:

Input:
S = "001"
Output: 1
Explanation: 
We can flip the 0th bit to 1 to have
101.


Example 2:

Input:
S = "0001010111" 
Output: 2
Explanation: We can flip the 1st and 8th bit 
bit to have "0101010101"
101."""

def minFlips(S):
    # Code here
    c1 = 0
    c2 = 0
    i = 0
    while i < len(S):
        if i%2 == 0 and S[i] == '0': c1+= 1
        elif i%2 != 0 and S[i] == '1': c1+=1
        elif i%2 == 0 and S[i] == '1': c2+=1
        elif i%2 != 0 and S[i] == '0': c2+=1
        i+= 1
    return min(c1,c2)

S = '0001010111'
print(minFlips(S))
