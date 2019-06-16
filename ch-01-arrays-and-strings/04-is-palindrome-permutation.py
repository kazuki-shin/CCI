# Determine whether or not a string is a permutation of a palindrome,
# ignoring spaces.

def is_palindrome_permutation(string):
    dict = {}
    for char in string:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    odd_cnt = 0
    for cnt in dict.values():
        if cnt % 2 == 1:
            odd_cnt += 1
    return not odd_cnt > 1

if __name__ == "__main__":
  import sys
  print(is_palindrome_permutation(sys.argv[-1]))


 # Notes:
 # A palindrome permutation can only have at most cgaracter that has an odd # of occurrences
 # Can be done in O(n) time and O(n) space
