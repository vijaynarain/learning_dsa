def check(str1,str2):
  l1 = len(str1)
  l2 = len(str2)
  if l1 != l2: return "false"
  mid = int(l1/2)
  if str1[:mid] == str2[mid:]:
    if str1[mid:] == str2[:mid]:
      return "true"
  return "false"
    

if __name__ == "__main__":
  str1 = "ABCDEF"
  str2 = "DEFABC"
  print(check(str1,str2))

"""
Algorithm:- 

1. first we chcking the length of two string which we are given. if the length are not same then we return False
2. secondly, we get the mid index for further process
3. Now we check, from start to mid index our string is same to mid to end index of second string
4. again we cheking this but in diffrent order str1[mid:] == str1[:mid]
5. if it passes both the cases than we return True, and if not than we passes False

"""