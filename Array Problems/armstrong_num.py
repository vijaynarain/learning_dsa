def check_arm(number):
  sum = 0
  original = number
  while number > 0:
    digit = number % 10
    sum += digit ** n
    number = number // 10

  if sum == original:
    print("True")
  else:
    print("False")

if __name__ == "__main__":
  number = int(input("Enter = "))
  n = len(str(number))
  check_arm(number)