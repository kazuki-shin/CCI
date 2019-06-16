# Replace spaces in the middle of a string with "%20" in place

def escape_spaces(s):
    string = list(s)
    currIdx = len(string)-1
    copyIdx = currIdx
    while string[copyIdx] == " ":
      copyIdx -= 1

    while copyIdx >= 0:
        if string[copyIdx] == " ":
             string[currIdx] = "0"
             string[currIdx-1] = "2"
             string[currIdx-2] = "%"
             currIdx -= 2
        else:
            string[currIdx] = string[copyIdx]

        currIdx -= 1
        copyIdx -= 1
    return ''.join(string)

if __name__ == "__main__":
  import sys
  print(escape_spaces("Mr John Smith    "))
