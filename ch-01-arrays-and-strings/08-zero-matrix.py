# Given a matrix, zero out every row and column that contains a zero.

import unittest

def zero_out_row_col(mat):


class Test(unittest.TestCase):
  def test_zero_out_row_col_matrix(self):
    mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
    zero_out_row_col(mat1)
    self.assertEqual(mat1, mat2)

if __name__ == "__main__":
  unittest.main()
