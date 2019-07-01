# Find a route from the first node to the second node in a directed graph.

def find_route(node1, node2):


class Node():
  def __init__(self, data, adjacency_list=None):

  def add_edge_to(self, node):

  def __str__(self):

class Queue():
  def __init__(self):

  def add(self, item):

  def remove(self):

import unittest

def str_for(path):
  if not path: return str(path)
  return ''.join([str(n) for n in path])

class Test(unittest.TestCase):
  def test_find_route(self):
    node_j = Node('J')
    node_i = Node('I')
    node_h = Node('H')
    node_d = Node('D')
    node_f = Node('F', [node_i])
    node_b = Node('B', [node_j])
    node_g = Node('G', [node_d, node_h])
    node_c = Node('C', [node_g])
    node_a = Node('A', [node_b, node_c, node_d])
    node_e = Node('E', [node_f, node_a])
    node_d.add_edge_to(node_a)
    self.assertEqual(str_for(find_route(node_a, node_i)), 'None')
    self.assertEqual(str_for(find_route(node_a, node_j)), 'ABJ')
    node_h.add_edge_to(node_i)
    self.assertEqual(str_for(find_route(node_a, node_i)), 'ACGHI')

if __name__ == "__main__":
  unittest.main()
