"""
Validate an IP Address

Write a program to Validate an IPv4 Address. According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1 . The generalized form of an IPv4 address is (0-255).(0-255).(0-255).(0-255). Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.

Your task is  to complete the function isValid which returns 1 if the ip address is valid else returns 0. The function takes a string s as its only argument .

Example 1:

Input:
ip = 222.111.111.111
Output: 1
Example 2:

Input:
ip = 5555..555
Output: 0
Explanation: 5555..555 is not a valid
ip address, as the middle two portions
are missing.
"""

def isValid(s):
    #code here
    count = 0
    i,j = 0,0
    n = len(s)
    if n < 7: return 0 
    while j < n:
        if s[j] == '.':
            if s[i].isalpha():
                return 0
            if len(s[i:j]) < 1: return 0
            if len(s[i:j]) > 3: return 0
            substr = int(s[i:j])
            if int(j) - int(i) > 1:
                add = (int(s[i]) + int(s[j-1]))
                if add <=0 and i == 0: return 0
            if 255>=substr and substr>=0:
                count += 1
                i = j+1
            else:
                return 0
        j+=1
    if count == 3:
        return 1
    else:
        return 0




if __name__ == "__main__":
  arr = ['1.222.111.2', 'a.222.111.111', '0.0.0.0', '111..222.']
  for s in arr:
    print(isValid(s))