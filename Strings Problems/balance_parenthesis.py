def ispar(x):
        # code here
        if len(x) < 2: return 'false'
        data = [x[0]]
        for i in range(1,len(x)):
            if x[i] == "{":
                data.append(x[i])
            elif x[i] == "(":
                data.append(x[i])
            elif x[i] == "[":
                data.append(x[i])
            
            else:
                if x[i] == "]":
                    if data[-1] == "[":
                        data.pop()
                    else:
                        return 'false'
                elif x[i] == ")":
                    if data[-1] == "(":
                        data.pop()
                    else:
                        return 'false'
                elif x[i] == "}":
                    if data[-1] == "{":
                        data.pop()
                    else:
                        return 'false'
        if not data:
            return 'true'
        else:
            return 'false'

if __name__ == "__main__":
  x = "{([])}()"
  print(ispar(x))

"""
Main Algo Explanation:- 

1. first you have to check is this have less than 2 parenthesis, if it's have than return false
2. second you have to store the first parenthesis in a new list
3. then you have to append the open parenthesis in the new list i.e. "( { ["
4. if you got close parenthesis than you have to check that is this parenthesis is closing the last value append i.e. ( == ) 
5. if this is true than pop the last value using .pop() 
6. if this is wrong than return false
7. finally after reading all the value, now you have to check that is this our new list is empty or not. because
if out parenthesis is balanced than our list have to empty and if our list is not empty than our parenthesis is not balanced and return false
"""