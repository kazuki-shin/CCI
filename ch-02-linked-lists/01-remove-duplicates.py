# Remove the duplicate values from a linked list.

import unittest

def remove_duplicates(head):
    node = head
    if node:
        values = {node.data = }

class Node():
  def __init__(self, data, next):
      self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_remove_duplicates(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_duplicates(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)

if __name__ == "__main__":
  unittest.main()
