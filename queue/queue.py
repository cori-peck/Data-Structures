class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    self.size += 1

  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop(0)
    else:
      return None

  def len(self):
    return self.size
