#here we implement queue using collection and dequeue

from collections import deque

class Queue:

  def __init__(self):
    self.container = deque()

  def enqueue(self,val):
    return self.container.appendleft(val)

  def dequeue(self):
    return self.container.pop()

  def peek(self):
    return self.container[-1]

  def size(self):
    return len(self.container)

  def isEmpty(self):
    return len(self.container) == 0

  def display(self):
    print(".....")
    for i in range(len(self.container)):
      print(self.container[i])
    print(".....")

a = Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.display()
print("front =",a.peek())
a.dequeue()
a.display()
print("front =",a.peek())

