# Return all downward paths through a tree whose nodes sum to a target value.

def paths_with_sum(binary_tree, target_sum):

def paths_with_partial_sum(node, target_sum, partial_paths):

class Node():
  def __init__(self, name, value, left=None, right=None):

class ListDict(dict):

import unittest

class Test(unittest.TestCase):
  def test_paths_with_sum(self):
    bt=Node("A",4,Node("B",-2,Node("D",7),Node("E", 4)),
                  Node("C", 7,Node("F",-1,Node("H",-1),Node("I",2,Node("K",1))),
                              Node("G", 0,None,        Node("J", -2))))
    self.assertEqual(paths_with_sum(bt, 12), [["A", "C", "F", "I"]])
    self.assertEqual(paths_with_sum(bt, 2), [["A", "B"], ["B", "E"], ["I"],
        ["F", "I", "K"]])
    self.assertEqual(paths_with_sum(bt, 9), [["A","B","D"], ["A","C","F","H"],
        ["C","F","I","K"], ["A","C","G","J"]])

if __name__ == "__main__":
  unittest.main()
