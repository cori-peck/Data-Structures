class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    deleted_item = self.storage[0]
    del self.storage[0]
    self._sift_down(0)
    return deleted_item

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    left = (2 * index) + 1
    right = (2 * index) + 2
    max_heap = index
    if len(self.storage) > left and self.storage[max_heap] < self.storage[left]:
      max_heap = left
    if len(self.storage) > right and self.storage[max_heap] < self.storage[right]:
      max_heap = right
    if max_heap == index:
      return

    else:
      sub = self.storage[index]
      self.storage[index] = self.storage[max_heap]
      self.storage[max_heap] = sub
      self._sift_down(max_heap)

