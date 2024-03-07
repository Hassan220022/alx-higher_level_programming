#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bor3i = []
    for i in my_list:
        if i % 2 == 0:
            bor3i.append(True)
        else:
            bor3i.append(False)
    return bor3i