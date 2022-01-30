class Node:
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

class Linkedlist:
  def __init__(self):
    self.head = Node(a[0],None)

  def reverse(self):
    itr = self.head
    while itr:
      print(itr.data)
      itr = itr.next
    
      
    
    
    


if __name__ == "__main__":
  a = [1,2,3,4,5]
  a = Linkedlist()
  a.reverse()
  

