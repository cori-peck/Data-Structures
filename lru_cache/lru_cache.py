from doubly_linked_list import DoublyLinkedList

class LRUCache:
  def __init__(self, limit=10):
    self.list = DoublyLinkedList()
    self.cache = {}
    self.limit = limit
    
  def get(self, key):
    if key in self.cache.keys():
      node = self.list.head
      while node.value != key:
        node = node.next
      self.list.move_to_end(node)
      return self.cache[key]
    else:
      return None
      
  def set(self, key, value):
    if len(self.cache.keys()) == 0:
      self.cache[key] = value
    elif key in self.cache.keys():
      self.cache[key] = value
      node = self.list.head
      while node.value != key:
        node = node.next
      self.list.move_to_end(node)
    elif len(self.cache.keys()) == self.limit:
      del self.cache[self.list.head.value]
      self.list.remove_from_head()
      self.list.add_to_tail(key)
      self.cache[key] = value
    else:
      self.list.add_to_tail(key)
      self.cache[key] =value