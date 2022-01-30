#working on this code

def Merge(l,mid,r):
    i = l
    j = mid + 1
    k = l
    while i <= mid and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1
    if i > mid:
        while j <= r:
            b[k] = a[j]
            k += 1
            j += 1
    else:
        while i <= mid:
            b[k] = a[i]
            k += 1
            i += 1
    print(b)

def MergeSort(l,r):
    if l < r:
        mid = int((l+r)/2)
        MergeSort(l,mid)
        MergeSort(mid+1,r)
        Merge(l,mid,r)

if __name__ == "__main__":
    a = [5,2,4,6,1,3,2,6]
    print(a)
    n = len(a)
    r = n - 1
    l = 0
    b = [0] * n
    MergeSort(l,r)
    print(b)