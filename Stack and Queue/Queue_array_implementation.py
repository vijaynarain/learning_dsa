#here we are going to implement queue with the help of array

def enqueue(val):
  global front,rear
  if(rear == size - 1):
    print("stack overflow")
  elif front == -1 and rear == -1:
    front = rear = 0
    queue[rear] = val
  else:
    rear += 1
    queue[rear] = val

def display():
  global front,rear
  if(front == -1 and rear == -1):
    print("queue is empty")
  else:
    for i in range(front,rear+1):
      print(queue[i])

def dequeue():
  global front,rear
  if(front == -1 and rear == -1):
    print("queue is empty")
  elif front == rear:
    front = rear = -1
  else:
    front += 1   

def peek():
  global front,rear
  if(front == -1 and rear == -1):
    print("queue is empty")
  else:
    print("top =",queue[front]) 

    




if __name__ == "__main__":
  queue = [None] * 5
  size = len(queue)
  front = rear = -1
  enqueue(1)
  enqueue(2)
  enqueue(3)
  dequeue()
  peek()
  display()
  