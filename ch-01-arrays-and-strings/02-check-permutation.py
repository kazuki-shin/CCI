# Determine whether or not one string is a permutation of another.

def is_permutation(str1, str2):
    dict = {}
    for letter in str1:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    for letter2 in str2:
        if letter2 not in dict:
            return False
        dict[letter2] -= 1
    return all(x==0 for x in dict.values())

if __name__ == "__main__":
  import sys
  print(is_permutation(sys.argv[-2], sys.argv[-1]))
