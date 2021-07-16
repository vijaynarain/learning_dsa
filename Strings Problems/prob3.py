"""
Roman Number to Integer 

Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5
Example 2:

Input:
s = III 
Output: 3
"""

def romanToDecimal(str):
    # code here
    if len(str) == 0: return None
    roman = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    result = 0
    #print(len(str))
    for i in range(len(str)):
        if len(str) < 2:
            result = roman[str[i]]
            return result
        key1 = str[i]
        if i < len(str)-1:
          key2 = str[i+1]
        else:
          key2 = str[i]
        #print(key1)
        #print(key2)
        if roman[key1] >= roman[key2]:
            result += roman[key1]
        else:
            result -= roman[key1]
    return result

if __name__ == "__main__":
  str = "MCMXCIV"
  print(romanToDecimal(str))
