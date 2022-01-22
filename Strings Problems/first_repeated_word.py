from collections import Counter


def firstRepeatedWord(S):
  S = list(S.split(" "))
  #print(S)
  times = Counter(S)
  #print(times)
  for i in S:
    if times[i] > 1:
      return i
           

S = "Vijay had been saying that he had been there"
print(firstRepeatedWord(S))