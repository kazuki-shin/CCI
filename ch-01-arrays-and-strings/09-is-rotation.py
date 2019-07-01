# Determine whether or not a given string is a rotation of another string.

import unittest

def is_rotation(s1, s2):
    tmp = s1+s1
    return is_substring(tmp,s2)

def is_substring(s1, s2):
    idx1 = 0
    idx2 = 0
    if s1 == s2:
        return True
    while idx1 < len(s1):
        if s1[idx1] == s2[idx2]:
            idx2+=1
        if idx2 == len(s2):
            return True
        idx1+=1
    return False

class Test(unittest.TestCase):
  def test_is_rotation(self):
    s1 = "tabletop"
    s2 = "toptable"
    s3 = "optalbet"
    self.assertTrue(is_rotation(s1, s2))
    self.assertFalse(is_rotation(s1, s3))

  def test_is_substring(self):
    s1 = "cat in the hat"
    s2 = "cat"
    s3 = "hat"
    s4 = "cats"
    self.assertTrue(is_substring(s1, s2))
    self.assertTrue(is_substring(s1, s3))
    self.assertFalse(is_substring(s1, s4))

if __name__ == "__main__":
  unittest.main()
