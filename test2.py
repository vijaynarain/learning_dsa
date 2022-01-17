def lps(p):
    lps = [0] * len(p)
    i = 1
    j = 0
    while i < len(p):
        if p[i] == p[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            lps[i] = 0
            j = lps[j-1]
            i += 1
    print(lps)
    print(j)
    return lps[-1]