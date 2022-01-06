def reverse(str):
  str1 = ""
  for i in range(1,len(str)+1):
    str1 += str[-i]
  str = str1
  return str
  

if __name__ == "__main__":
  str = "ABCDE"
  print(reverse(str))