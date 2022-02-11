"""
Input:
N = 3
value[] = {1,3,4}
x = 2
Output: True
Explanation: In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.
"""

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

  def detect_loop(self):
    s = set()
    temp = self.head
    while temp != None:
      if temp in s:
        return True
      s.add(temp)
      temp = temp.next

    return False


    # Driver program for testing
llist = LinkedList()
llist.insert_at_start(20)
llist.insert_list([4,15,10])
 
# Create a loop for testing
llist.head.next.next.next.next = llist.head
 
if(llist.detect_loop()):
    print("Loop found")
else:
    print("No Loop ")