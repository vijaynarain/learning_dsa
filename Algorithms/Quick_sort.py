def Swap(i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def Partition(l,h):
    pivet = a[l]
    i = l
    j = h
    while i < j:
        while a[i] <= pivet and i<h: i+= 1
        while a[j] > pivet and j > 0: j-= 1
        if i < j:
            Swap(i,j)
    Swap(j,l)
    return j

def Quicksort(l,h):
    if l < h:
        pivet = Partition(l,h)
        Quicksort(l,pivet-1)
        Quicksort(pivet+1,h)

if __name__ == "__main__":
    a = [4,6,2,5,7,9,1,3]
    n = len(a)
    h = n - 1
    l = 0
    Quicksort(l,h)
    print(a)
    
    
