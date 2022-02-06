from collections import Counter
"""
Majority Element

Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

Examples : 

Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater
than the half of the size of the array size. 

Input : {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is
greater than the half of the size of the array size.
"""

#old code
"""
def majorityCheck():
    fq = len(a) / 2
    for i in range(len(a)):
        times = 0
        for j in range(1, len(a)):
            if a[i] == a[j]:
                times += 1
        if times > fq:
            return (
                f"The frequency of {a[i]} is {times} which is greater than the half of the size of the array size"
            )

    return ("No Majority Element")
"""

#new code
def majorityCheck():
  times = Counter(a)
  for i in times:
    if times[i] > int(len(a)/2):
      return "Majority Element",i
  return "No Majority Element"

if __name__ == "__main__":
    a = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print(majorityCheck())
