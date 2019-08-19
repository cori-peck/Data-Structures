class Node:
  def __init__(self, value, next_node=None):
    self.value = value 
    self.next_node = next_node

  def make_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
    def add_to_tail(self, value):
      new_node = Node(value)
      
      if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
      else:
        new_node.prev = self.tail
        self.tail.make_next(new_node)
        self.tail = new_node


    def remove_from_head(self):
      value = self.head.value
      self.delete(self.head)
      return value




class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    return self.storage.add_to_tail(item)
  
  def dequeue(self):
    pass

  def len(self):
    return self.size
