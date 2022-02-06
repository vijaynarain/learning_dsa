"""
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5 
Explanation: 
The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.

Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4 
Explanation: 
The first 3 elements are 1,2,3 are reversed 
first and then elements 4,5 are reversed.Hence, 
the resultant linked list is 3->2->1->5->4.
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

  def reverse(self,head,k):
    if head is None:
      return "LinkedList is empty"
    curr = head
    prev = None
    temp = None
    count = 0
    while curr is not None and count < k:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
      count += 1

    if temp is not None:
      head.next = self.reverse(temp,k)

    return prev
    itr = prev
    ilstr = ""
    while itr:
      ilstr += str(itr.data) + "->"
      itr = itr.next
    print(ilstr)
    

l = LinkedList()
l.insert_at_start(1)
l.insert_list([2,2,4,5,6,7,8])
l.print()
l.head = l.reverse(l.head,k=4)
l.print()
