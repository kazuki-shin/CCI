# Create a minimal height binary search tree with the elements of a given
# sorted array.

def minimal_height_bst(sorted_array):


class BSTNode():
  def __init__(self, data=None, left=None, right=None):

  def __str__(self):

import unittest

class Test(unittest.TestCase):
  def test_minimal_height_bst(self):
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bst = minimal_height_bst(sorted_array)
    self.assertEqual(str(bst), "(5(3(2(1..).)(4..))(8(7(6..).)(9..)))")

if __name__ == "__main__":
  unittest.main()
