# Determine a build order given a list of projects and their dependencies.

def build_order(projects, dependencies):


class GraphNode():
  def __init__(self, data):

  def add_edge(self, node):


class Queue():
  def __init__(self):
  def add(self, item):
  def remove(self):
  def is_not_empty(self): 

import unittest

class Test(unittest.TestCase):
  def test_build_order(self):
    projects = ["A", "B", "C", "D", "E", "F", "G"]
    dependencies1 = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
        ("A", "E"), ("B", "E"), ("D", "G")]
    self.assertEqual(build_order(projects, dependencies1),
        ["D", "F", "G", "B", "C", "A", "E"])
    dependencies2 = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
    self.assertEqual(build_order(projects, dependencies2).__class__, Exception)
    dependencies3 = [("A", "B"), ("A", "C"), ("E", "A"), ("E", "B"), ("A", "F"),
        ("B", "F"), ("C", "F"), ("G", "D")]
    self.assertEqual(build_order(projects, dependencies3),
        ["E", "G", "A", "D", "B", "C", "F"])

if __name__ == "__main__":
  unittest.main()
