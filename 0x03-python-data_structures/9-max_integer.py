#!/usr/bin/pythone
def max_integer(my_list=[]):
    max = my_list[0]
    for i in my_list:
        if max < i:
            max = i
    return max