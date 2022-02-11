"""
*Important

Implement two stacks in an array

Create a data structure twoStacks that represents two stacks. Implementation of twoStacks should use only one array, i.e., both stacks use the same array for storing elements. Following functions must be supported by twoStacks.
push1(int x) –> pushes x to first stack 
push2(int x) –> pushes x to second stack
pop1() –> pops an element from first stack and return the popped element 
pop2() –> pops an element from second stack and return the popped element
Implementation of twoStack should be space efficient.
"""

class twoStack:

  def __init__(self, n):
    self.size = n
    self.arr = [None] * n
    self.top1 = -1
    self.top2 = self.size

  def push1(self, x):
    if self.top1 < self.top2 - 1:
      self.top1 = self.top1 + 1
      self.arr[self.top1] = x
    else:
      print("Stack Overflow ")
      exit(1)

  def push2(self, x):
    if self.top2 < self.top2 - 1:
      self.top2 = self.top2 - 1
      self.arr[self.top2]= x
    else:
      print("Stack Overflow ")
      exit(1)

  def pop1(self):
    if self.top1 >= 0:
      x = self.arr[self.top1]
      self.top1 = self.top1 - 1
      return x
    else:
      print("Stack Overflow ")
      exit(1)

  def pop2(self):
    if self.top2 < self.size:
      x = self.arr[self.top2]
      self.top2 = self + 1
      return x
    else:
      print("Stack Overflow ")
      exit(1)

obj = twoStack(6)

obj.push1(1)
obj.push2(6)
obj.push1(2)
obj.push2(3)
obj.push1(4)
obj.push2(5)

print(f"Popped element = {obj.pop1()}")

obj.push1(4)






