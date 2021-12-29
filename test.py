input_str = ['h','e','l','l','o']

end = -1
N = len(input_str)
for i in range(1,N+1):
  input_str[i-1],input_str[-i] = input_str[-i],input_str[i-1]
print(input_str)