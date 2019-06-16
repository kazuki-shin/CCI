# Compress a string made up of letters by replacing each substring containing
# a single type of letter by that letter followed by the count if the result
# is shorter than the original.

def compress(string):
    encoded = []
    curr_char = ""
    repeat = False
    rp_cnt = 1
    for idx in range(len(string)):
        repeat =  string[idx] == curr_char
        if not repeat:
            # if new char, add freq of last char
            if rp_cnt != 1:
                encoded.append(str(rp_cnt))
                rp_cnt = 1
            # set new focused char
            curr_char = string[idx]
            encoded.append(curr_char)
        else:
            rp_cnt += 1
            if idx == len(string)-1:
                encoded.append(str(rp_cnt))
    return ''.join(encoded)

if __name__ == "__main__":
  import sys
  print(compress(sys.argv[-1]))
