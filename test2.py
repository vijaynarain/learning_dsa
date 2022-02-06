class Node:
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_in_begining(self,data):
    node = Node(data,self.head)
    self.head = node

  def insert(self,data):
    if self.head is None:
      node = Node(data,None)
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(data,None)

  def insert_list(self,datalist):
    for data in datalist:
      self.insert(data)

  def get_lenght(self):
    if self.head is None:
      print("LinkedList is empty")
    itr = self.head
    count = 0
    while itr:
      itr = itr.next
      count += 1
    return count

  def remove_at(self,index):
    if index < 0 and index > self.get_lenght():
      print("ERROR, Change index value")
    itr = self.head
    count = 0
    while itr:
      while count == index - 1:
        itr.next = itr.next.next
        break
      count+=1
      itr = itr.next
    
      
    
      

  def print(self):
    if self.head is None:
      print("LinkedList is empty")
    itr = self.head
    ilstr = ''
    while itr:
      ilstr += str(itr.data) + '->'
      itr = itr.next
    print(ilstr)

l = LinkedList()
l.insert_in_begining(0)
l.insert(1)
l.insert(2)
l.insert_list([3,4,5,6,7,8,9,10])
print(l.get_lenght())
l.print()
l.remove_at(3)
l.print()