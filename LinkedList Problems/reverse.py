class Node:
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_start(self,data):
    node = Node(data,self.head)
    self.head = node

  def insert_at_end(self,data):
    if self.head is None:
      print("LinkedList is empty")
    node = Node(data,None)
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = node

  def insert_list(self,datalist):
    if self.head is None:
      print("LinkedList is empty")
    for data in datalist:
      self.insert_at_end(data)

  def print(self):
    if self.head is None:
      print("LinkedList is empty")
    itr = self.head
    ilstr = ""
    while itr:
      ilstr += str(itr.data) + "->"
      itr = itr.next
    print(ilstr)

  def reverse(self):
    curr = self.head
    prev = None
    while curr != None:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    itr = prev
    ilstr = ""
    while itr:
      ilstr += str(itr.data) + "->"
      itr = itr.next
    print(ilstr)
    

l = LinkedList()
l.insert_at_start(1)
l.insert_at_end(2)
l.insert_list([3,4,5])
l.print()
l.reverse()
