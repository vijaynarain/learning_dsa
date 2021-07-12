#program to sort an array in a assending format

a = [5, 20, 3, 67, 89, 2, 4, 10, 15]

print(f"Before sorting = {a}")

for i in range(len(a)):
  for j in range(i+1, len(a)):
    if a[i] > a[j]:
      a[i],a[j] = a[j],a[i]

print(f"After sorting = {a}")