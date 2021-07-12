#reverse the given array

a = [1, 2, 3, 4, 5, 6]
b= []


for i in range(len(a)):
  b.append(a[-1-i])

print(b)