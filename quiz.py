"""
Create an application for quiz. Every time a user logs in, he should be asked for his name, the application should display the questions randomly. The user should be able to quit answering anytime. The score of the user should also be stored in the database.
"""

def quiz():
  rights = 0
  questions = ["1+2","3+1","5+6"]
  for i in questions:
    result = 0
    data = i.split("+")
    user = int(input(f"Enter the answer of this {i} = "))
    #print(data)
    for j in data:
      result += int(j)
      #print(result)
    if result == user:
      rights += 1
      print("you are right")
    elif user == 0:
      rights -= 1
      print("thank you for using")
      return
    else:
      print("you are wrong")
  print("Total Right Answer =",rights)
    

if __name__ == "__main__":
  quiz()
