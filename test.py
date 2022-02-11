def selectionsort(a):
  n = len(a)
  for i in range(n-1):
    min = i
    for j in range(i+1,n):
      if a[j] < a[min]:
        min = j
    if min != i:
      a[i],a[min] = a[min],a[i]
  print(a)

selectionsort([4,5,2,1,3])