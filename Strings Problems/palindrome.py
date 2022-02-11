def isPalindrome(self, S):
		# code here
		N = len(S)
		start = 0
		end = N - 1
    while start < end:
      if S[start] != S[end]:
        return 0
      start += 1
      end -= 1
    return 1

if __name__ == "__main__":
  str = "MAMAM"
  print(palindrome(str))

