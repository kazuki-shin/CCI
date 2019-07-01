# Sum two numbers that are represented with linked lists with decimal digits
# in reverse order of magnitude.

import unittest

def sum_lists(num1, num2):

class Node():
  def __init__(self, data, next=None):

  def __str__(self):

class Test(unittest.TestCase):
  def test_sum_lists(self):
    num1 = Node(1,Node(2,Node(3)))
    num2 = Node(4,Node(9,Node(5)))
    self.assertEqual(str(sum_lists(num1, num2)), "5,1,9")
    num1 = Node(9,Node(2,Node(3,Node(4,Node(1)))))
    num2 = Node(4,Node(9,Node(8)))
    self.assertEqual(str(sum_lists(num1, num2)), "3,2,2,5,1")

if __name__ == "__main__":
  unittest.main()
