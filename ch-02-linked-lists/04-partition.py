# Partition a linked list so that all of the nodes containing values less than
# a pivot value occur before all of the nodes containing values greater than
# or equal to the pivot value.

import unittest

def partition(head, pivot):

class Node():
  def __init__(self, data, next=None):

  def __str__(self):

class Test(unittest.TestCase):
  def test_partition(self):
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    head2 = partition(head1, 6)
    self.assertEqual(str(head2), "2,1,3,7,9,6,8")
    head3 = partition(head2, 7)
    self.assertEqual(str(head3), "2,1,3,6,7,9,8")

if __name__ == "__main__":
  unittest.main()
