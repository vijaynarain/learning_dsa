def check_prime(n):
  if n < 2:
    print("Not prime number")
  else:
    for i in range(2,n):
      if n % i == 0:
        return "Not prime number"
  return "Number is prime"

n = int(input("Enter the number = "))
print(check_prime(n))