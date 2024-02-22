#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add

    count = len(sys.argv) - 1
    sum = 0
    for i in range(count):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))