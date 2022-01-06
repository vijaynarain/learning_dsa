def count_say(N):
  if N == 1: return "1"
  if N == 2: return "11"
  s = "11"
  for i in range(3,N+1):
    t = ""
    s = s + "&"
    count = 1
    for j in range(1,len(s)):
      if s[j-1] != s[j]:
        t = t + str(count)
        t = t + s[j-1]
        count = 1
      else:
        count += 1
    s = t
  return s

if __name__ == "__main__":
  N = 5
  print(count_say(N))