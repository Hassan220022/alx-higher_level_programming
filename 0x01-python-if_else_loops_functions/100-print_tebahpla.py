#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1,-1):
    if i % 2 == 1:
        print("{:s}".format(chr(i)), end="")
    else:
        print("{:s}".format(chr(i+32)), end="")
