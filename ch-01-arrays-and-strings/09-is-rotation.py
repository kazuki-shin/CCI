# Determine whether or not a given string is a rotation of another string.

import unittest

def is_rotation(s1, s2):

def is_substring(s1, s2):

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
