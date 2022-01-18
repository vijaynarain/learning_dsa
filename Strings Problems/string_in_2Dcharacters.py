"Count of number of given string in 2D character array"

def solve(i,j,s,ch,size,idx):
    found = 0
    if i>=0 and j>=0 and i<6 and j<6 and s[idx] == ch[i][j]:
        temp = s[idx]
        ch[i][j] = 0
        idx += 1
        if idx == size:
            found = 1
        else:
            found += solve(i+1,j,s,ch,size,idx)
            found += solve(i-1,j,s,ch,size,idx)
            found += solve(i,j+1,s,ch,size,idx)
            found += solve(i,j-1,s,ch,size,idx)
        ch[i][j] = temp
    return found


if __name__ == "__main__":
    s = "GEEKS"

    ch = [['D','D','D','G','D','D'],
          ['B','B','D','E','B','S'],
          ['B','S','K','E','B','K'],
          ['D','D','D','D','D','E'],
          ['D','D','D','D','D','E'],
          ['D','D','D','D','D','G']]

    ans = 0
    size = len(s)
    for i in range(6):
        for j in range(6):
            ans += solve(i,j,s,ch,size,0)

    print(ans)
