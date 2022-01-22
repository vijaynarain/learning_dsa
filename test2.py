if number <= N:
    increament = pow(10,math.floor(l/2))
    rundupNum = str(math.floor(math.floor(int(int(N)/increament) + 1) * increament))
    nextPalin(rundupNum)