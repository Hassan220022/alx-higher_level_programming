#!/usr/bin/pythone
def max_integer(my_list=[]):
    max = my_list[0]
    if not max:
        return None
    else:
        for i in my_list:
            if max < i:
                max = i
        return max
