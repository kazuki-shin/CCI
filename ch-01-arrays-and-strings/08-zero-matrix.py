# Given a matrix, zero out every row and column that contains a zero.

import unittest

def zero_out_row_col(mat):
    n = len(mat)
    if n == 0:
        return mat
    m = len(mat[0])
    zero_row, zero_col = [],[]
    for row in range(n):
        for col in range(m):
            if mat[row][col] == 0:
                zero_row.append(row)
                zero_col.append(col)
                break
    for row in zero_row:
        for col in range(m):
            mat[row][col] = 0
    for row in range(n):
        for col in zero_col:
            mat[row][col] = 0

class Test(unittest.TestCase):
  def test_zero_out_row_col_matrix(self):
    mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
    zero_out_row_col(mat1)
    self.assertEqual(mat1, mat2)

if __name__ == "__main__":
  unittest.main()
