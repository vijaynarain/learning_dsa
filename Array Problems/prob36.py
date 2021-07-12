"""
Stock Buy Sell to Maximize Profit

The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
"""

def maximumProfit():
  profit = 0
  for i in range(1,n):
    if a[i-1] < a[i]:
      profit += (a[i] - a[i-1])
  return profit


if __name__ == "__main__":
  a = [100, 180, 260, 310, 40, 535, 695]
  n = len(a)
  print(maximumProfit())