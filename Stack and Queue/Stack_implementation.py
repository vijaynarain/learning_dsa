#here we are going to implement the stack

from collections import deque

class Stack:

  def __init__(self):
    self.container = deque()

  def push(self,val):
    self.container.append(val)

  def pop(self):
    return self.container.pop()

  def peek(self):
    return self.container[-1]

  def isEmpty(self):
    return len(self.container) == 0

  def size(self):
    return len(self.container)

  def display(self):
    print("......")
    for i in range(len(self.container)):
      print(self.container[i])
    print("......")

  
a = Stack()

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.display()
a.pop()
a.pop()
a.display()
print(a.peek())
print(a.isEmpty())
print(a.size())