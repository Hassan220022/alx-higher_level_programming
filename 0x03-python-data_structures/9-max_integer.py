#!/usr/bin/pythone
def max_integer(my_list=[]):
    if len(my_list):
        max = my_list[0]
        for i in range(len(my_list)):
            if max < my_list[i]:
                max = my_list[i]
        return max
    return None
