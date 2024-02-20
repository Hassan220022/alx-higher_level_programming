#!/usr/bin/python3
for letter in range(ord('a'), ord('z')+1):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{:s}".format(chr(letter)), end="")
    else:
        continue
