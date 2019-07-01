# Design a binary tree class that can return a random node.

class Node():
  def __init__(self, data=None, left=None, right=None):

  def get_random_node(self):

  def get_numbered_node(self, number):

import random
import unittest

mock_random_value = False

def randint(lower_bound, upper_bound):

class Test(unittest.TestCase):
  def test_mock_randint(self):
    global mock_random_value
    mock_random_value = 12
    self.assertEqual(randint(0, 2000), 12)

  def test_get_random_value(self):
    global mock_random_value
    tree = Node(11,Node(21,Node(31),Node(32,Node(41),Node(42,None,Node(51)))),
                   Node(22,Node(33),Node(34)))
    mock_random_value = 0
    self.assertEqual(tree.get_random_node().data, 11)
    mock_random_value = 4
    self.assertEqual(tree.get_random_node().data, 41)
    mock_random_value = 8
    self.assertEqual(tree.get_random_node().data, 33)

if __name__ == "__main__":
  unittest.main()
