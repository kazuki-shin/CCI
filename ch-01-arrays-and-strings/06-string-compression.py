# Compress a string made up of letters by replacing each substring containing
# a single type of letter by that letter followed by the count if the result
# is shorter than the original.

# approach: put all chars in dict,
def compress(string):
  dict = {}
  for char in string:
    if char not in dict:
      dict[char] = 1
    else:
      dict[char] += 1
  encoded = []
  for key, value in dict.items():
    if value == 1:
      encoded.append(key)
    elif value == 2:
      encoded.append(key)
      encoded.append(key)
    else:
      encoded.append(key)
      encoded.append(value)
  return ''.join(encoded)

if __name__ == "__main__":
  import sys
  print(compress(sys.argv[-1]))
