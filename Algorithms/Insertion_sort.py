def insertionSort(a,n):
    for i in range(1,n):
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    
    return a

print(insertionSort([8,4,1,5,9,2],6))
