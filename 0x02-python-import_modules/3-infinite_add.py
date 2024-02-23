#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = len(sys.argv) - 1
    sum = 0
    for i in range(counter):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
