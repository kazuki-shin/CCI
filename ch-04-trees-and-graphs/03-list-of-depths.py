# Return an array of linked lists containing all elements on each depth
# of a binary tree.

def list_of_depths(binary_tree):

class TreeNode():
  def __init__(self, data=None, left=None, right=None):

class ListNode():
  def __init__(self, data=None, next=None):

  def __str__(self):

class Queue():
  def __init__(self):

  def add(self, item):

  def remove(self):

import unittest

class Test(unittest.TestCase):
  def test_list_of_depths(self):
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    lists = list_of_depths(node_a)
    self.assertEqual(str(lists[0]), "A,None")
    self.assertEqual(str(lists[1]), "B,C,None")
    self.assertEqual(str(lists[2]), "D,E,F,None")
    self.assertEqual(str(lists[3]), "H,G,None")
    self.assertEqual(len(lists), 4)

if __name__ == "__main__":
  unittest.main()
