"""
Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.

Examples : 

Input : 100
Output : 933262154439441526816992388562667004-
         907159682643816214685929638952175999-
         932299156089414639761565182862536979-
         208272237582511852109168640000000000-
         00000000000000

Input :50
Output : 3041409320171337804361260816606476884-
         4377641568960512000000000000
"""

def factorial():
  n = 1
  fact = a
  while True:
    if(a - n) == 0:
      break
    fact = fact * (a - n)
    n += 1
  return fact


if __name__ == "__main__":
  a = int(input("Enter the number which you want factorial of = "))
  print(f"Factorial of {a} = {factorial()}")
