"""
Implement Atoi

Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.

Note: You are not allowed to use inbuilt function.

Example 1:

Input:
str = 123
Output: 123

Example 2:

Input:
str = 21a
Output: -1
Explanation: Output is -1 as all
characters are not digit only.
"""

def atoi(str):
  data = ''
  i = 1
  for j in range(i,len(str)):
      if str[j].isdigit():
        data += str[j]
      else:
        return -1
  return int(str[0]+data)
  

if __name__ == "__main__":
  str = "12"
  print(atoi(str))