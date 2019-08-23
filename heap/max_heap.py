class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    last_index = self.get_size()-1
    self.storage[0], self.storage[last_index] = self.storage[last_index], self.storage[0]
    deleted_item = self.storage.pop()
    self._sift_down(0)
    return deleted_item

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if (self.storage[index] > self.storage[parent] and index > 0):
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent

      else:
        break

  def _sift_down(self, index):
    left = (2 * index) + 1
    right = (2 * index) + 2

    if left < self.get_size():
      if right < self.get_size():
        if self.storage[left] < self.storage[right]:
          left = right
        if self.storage[index] < self.storage[left]:
          self.storage[index], self.storage[left] = self.storage[left], self.storage[index]
          self._sift_down(left)

