from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = DoublyLinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1

  def dequeue(self):
    if self.size > 0:
      self.size -= 1
    else:
      return None

    return self.storage.remove_from_head()

  def len(self):
    return self.size
