# Return an intersecting node if two linked lists intersect.

import unittest

def intersection(head1, head2):


class Node():
  def __init__(self, data, next=None):

  def __str__(self):

class Test(unittest.TestCase):
  def test_intersection(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(intersection(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(intersection(head3, head4), node)

if __name__ == "__main__":
  unittest.main()
