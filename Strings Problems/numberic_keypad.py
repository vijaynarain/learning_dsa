"Convert a sentence into its equivalent mobile numeric keypad sequence"

def numberic(data,text):
  n = len(text)
  output = ""
  for i in range(n):
    if text[i] == ' ':
      output = output + '0' #for space in text we add 0 in output
    else:
      position = ord(text[i]) - ord('A') #to get position in data
      output = output + data[position] 
      
  return output

data = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]

text = "HELLO WORLD"
print(numberic(data,text))