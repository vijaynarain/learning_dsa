def SelectionSort(a,n):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[j] < a[min]:
                min = j
        if min != i:
            a[i],a[min] = a[min],a[i]
    
    return a

print(SelectionSort([8,4,1,5,9,2],6))
