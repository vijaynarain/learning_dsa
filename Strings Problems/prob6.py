"""
Smallest window in a string containing all the characters of another string

Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. 

Example 1:

Input:
S = "timetopractice"
P = "toc"
Output: toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.
Example 2:

Input:
S = "zoomlazapzo"
P = "oza"
Output: apzo
Explanation: "apzo" is the smallest 
substring in which "oza" can be found.
"""

def smallestWindow(s,p):
  table = {}
  times = 1
  start = 0
  j  = 0
  count = 0
  min_length = 999999
  #table updating code
  for i in range(len(p)):
    if p[i] in table:
      times += 1
      table.update({f"{p[i]}" : times})
    else:
      times = 1
      table.update({f"{p[i]}" : times})
  #table checking and count updating code
  while count <= len(p) and j < len(s):
    if s[j] in table:
      if table[f"{s[j]}"] > 0:
        count += 1
      times = table[f"{s[j]}"] - 1 
      table.update({f"{s[j]}" : times})
    #you got all given elements
    if count == len(p):
      length = j - start
      if min_length > length:
        min_length = length
        #print(min_length)
        #print(s[start:min_length+1])
        #print(table)
      while count == len(p):
        start += 1
        if s[start-1] in table and table[f"{s[start-1]}"] <= 0:
          times = table[f"{s[start-1]}"] + 1 
          table.update({f"{s[start-1]}" : times})
          #print(s[start-1:j+1])
          #print(table)
          if times > 0:
            count -= 1
          #print(count)

    
    j += 1

  #print(count)
  return s[start-1:j+1]


if __name__ == "__main__":
  s = "zoomlazapzo"
  p = "oza"
  print(smallestWindow(s,p))

