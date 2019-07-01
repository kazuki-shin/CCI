# Determine whether one binary tree is a subtree of another.

def is_subtree(bt1, bt2):

def equivalent_trees(bt1, bt2):

class Node():
  def __init__(self, data=None, left=None, right=None):

def tree_generator(node):

import unittest

class Test(unittest.TestCase):
  def test_is_subtree(self):
    tree1 = Node(5,Node(3,Node(2),Node(4)),Node(8,Node(7,Node(9)),Node(1)))
    tree2 = Node(8,Node(7),Node(1))
    self.assertEqual(is_subtree(tree1, tree2), False)
    tree3 = Node(8,Node(7,Node(9)),Node(1))
    self.assertEqual(is_subtree(tree1, tree3), True)

if __name__ == "__main__":
  unittest.main()
