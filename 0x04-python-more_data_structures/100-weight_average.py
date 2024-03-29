#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        numerator = sum([score * weight for score, weight in my_list])
        denominator = sum([weight for score, weight in my_list])
        return (numerator / denominator)
