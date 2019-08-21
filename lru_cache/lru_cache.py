from doubly_linked_list import DoublyLinkedList

class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.size = 0
    self.storage = dict()
    self.order = DoublyLinkedList()

  def get(self, key):
    if key in self.storage:
      node = self.storage[key]
      self.order.move_to_front(node)
      return node.value[1]

    else:
      return None

  def set(self, key, value):
    if key in self.storage:
      node = self.storage[key]
      node.value = (key, value)
      self.order.move_to_front(node)
      return

    if self.size == self.limit:
      del self.storage[self.order.tail.value[0]]
      self.order.remove_from_tail()
      self.size -= 1

    self.order.add_to_head((key, value))
    self.storage[key] = self.order.head
    self.size += 1
