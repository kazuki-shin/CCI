# Determine whether or not a linked list is a palindrome.

import unittest

def is_palindrome(head):


def copy_reverse(head):


def copy(node):


class Node():
  def __init__(self, data, next=None):

  def __str__(self):

class Test(unittest.TestCase):
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome(list4))

  def test_copy_reverse(self):
    head = Node(10,Node(20,Node(30,Node(40))))
    self.assertEqual(str(copy_reverse(head)), "40,30,20,10")

if __name__ == "__main__":
  unittest.main()
