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

  def print(self):
    if self.head is None:
      print("LinkedList is empty")
      return 
    itr = self.head
    llstr = ''

    while itr:
      llstr += str(itr.data) + " "
      itr = itr.next
    print(llstr)

  def insert_at_end(self,data):
    if self.head is None:
      self.head = Node(data,None)
      return
    itr = self.head
    
    while itr.next:
      itr = itr.next
    itr.next = Node(data,None)

  def insert_values(self,data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)

  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      itr = itr.next
      count +=1
    return count

  def remove_at(self,index):
    if index < 0 or index >= self.get_length():
      raise Exception("Invalid index")
    if index == 0:
      self.head = self.head.next
    count = 0
    itr = self.head
    while itr:
      while count == index - 1:
        itr.next = itr.next.next
        break
      count+=1
      itr = itr.next

  def insert_at(self,index,data):
    if index < 0 or index >= self.get_length():
      raise Exception("Invalid Index")
    if index == 0:
      self.insert_in_begining(data)

    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        node = Node(data, itr.next)
        itr.next = node
        break
      itr = itr.next
      count += 1

if __name__ == "__main__":
  mylist = LinkedList()
  mylist.insert_values([10,20,30,40])
  print("length",mylist.get_length())
  mylist.print()
  mylist.remove_at(2)
  mylist.print()
  mylist.insert_at(1,100)
  mylist.print()